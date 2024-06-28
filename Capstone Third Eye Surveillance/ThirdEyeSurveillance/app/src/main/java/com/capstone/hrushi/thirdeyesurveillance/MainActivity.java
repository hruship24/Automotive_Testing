package com.capstone.hrushi.thirdeyesurveillance;

import android.Manifest;

import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.location.Location;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Bundle;

import android.provider.MediaStore;
import android.util.Log;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.work.OneTimeWorkRequest;
import androidx.work.WorkManager;

import java.io.IOException;

public class MainActivity extends AppCompatActivity implements VibrationDetector.VibrationListener{

    private static final String TAG = "MainActivity";
    private static final int CAMERA_PERMISSION_CODE = 100;
    private static final int REQUEST_CAMERA = 101; // Request code for launching camera activity
    private static final int REQUEST_IMAGE_CAPTURE = 102; // Request code for Image Capture
    private static final int REQUEST_VIDEO_CAPTURE = 103; // Request code for Video Capture

    private VibrationDetector vibrationDetector;
    private boolean isCapturing = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Initialize the vibration Detector
        vibrationDetector = new VibrationDetector(this, (VibrationDetector.VibrationListener) this);

        if (checkPermission()) { // Check if the Camera permission is granted
            // Permission is granted, initialize your camera functionality
            Log.d(TAG, "Camera permission granted");
            openCamera();
            //uncomment this to run vibration detection
            //vibrationDetector.start(); // Start the vibration Detector
        } else {
            requestPermission(); // Request permission is not granted
        }
    }

    private boolean checkPermission() {
        int cameraPermission = ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA);
        return cameraPermission == PackageManager.PERMISSION_GRANTED;
    }

    private void requestPermission() {
        ActivityCompat.requestPermissions(this,
                new String[]{Manifest.permission.CAMERA},
                CAMERA_PERMISSION_CODE);
    }

    private void openCamera() {
        // Assuming you have a method to open camera or perform camera-related tasks
        // Example: Opening camera using Intent
        try {
//            // Launching camera using intent
//            Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
//            startActivityForResult(intent, REQUEST_CAMERA);
//            Toast.makeText(this, "Camera opened successfully", Toast.LENGTH_SHORT).show();

            Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);

            // Launching camera application for Capturing Image
            if (intent.resolveActivity(getPackageManager()) != null) {
                startActivityForResult(intent, REQUEST_IMAGE_CAPTURE);
                Toast.makeText(this, "Camera opened for image capture", Toast.LENGTH_SHORT).show();
            } else {
                Log.e(TAG, "No camera app available to handle the request.");
                Toast.makeText(this, "No camera app available", Toast.LENGTH_SHORT).show();
            }

            // Uncomment below for video recording
            /*
            Intent videoIntent = new Intent(MediaStore.ACTION_VIDEO_CAPTURE);
            startActivityForResult(videoIntent, REQUEST_VIDEO_CAPTURE);
            Toast.makeText(this, "Camera opened successfully for video recording", Toast.LENGTH_SHORT).show();
            */

        } catch (Exception e) {
            Log.e(TAG, "Error opening camera: " + e.getMessage());
            Toast.makeText(this, "Error opening camera", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == CAMERA_PERMISSION_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // Permission is granted, initialize your camera functionality
                Log.d(TAG, "Camera permission granted");
                //openCamera();

                vibrationDetector.start();
            } else {
                // Permission denied
                Log.d(TAG, "Camera permission denied");
                Toast.makeText(this, "Camera permission denied", Toast.LENGTH_SHORT).show();
            }
        }
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == RESULT_OK) {
            if (requestCode == REQUEST_IMAGE_CAPTURE) {
                Bundle extras = data.getExtras();
                Bitmap imageBitmap = (Bitmap) extras.get("data");
                // Handle the captured image
                Log.d(TAG, "Image captured successfully " );
                Toast.makeText(this, "Image captured successfully", Toast.LENGTH_SHORT).show();

                try {
                    Location currentLocation = getLastKnownLocation();
                    StorageHelper.saveCompressedImage(this, imageBitmap, currentLocation);
                    Toast.makeText(this, "Image Saved Successfully", Toast.LENGTH_SHORT).show();
                } catch (IOException e) {
                    Log.e(TAG, "Error saving image"+ e.getMessage());
                    Toast.makeText(this, "Error saving image", Toast.LENGTH_SHORT).show();
                }


                //Process and compress the image
                if(imageBitmap != null){
                    try {
                        ImageUtils.saveCompressedImage(this, imageBitmap);
                    } catch (IOException e) {
                        Log.e(TAG, "Error saving compressed image : "+ e.getMessage());
                        Toast.makeText(this, "Error saving compressed image", Toast.LENGTH_SHORT).show();

                    }
                }


            } else if (requestCode == REQUEST_VIDEO_CAPTURE) {
                Uri videoUri = data.getData();
                // Handle the captured video
                Log.d(TAG, "Video recorded successfully: " + videoUri.toString());
                Toast.makeText(this, "Video recorded successfully", Toast.LENGTH_SHORT).show();

                // Reset capturing flag after a short delay to allow for another capture
                new android.os.Handler().postDelayed(()-> isCapturing=false, 500);
            }
        }
        //isCapturing = false;
    }

    @Override
    public void onVibrationDetected(){
        Log.d(TAG, "Vibration Detected, Starting Camera Capture.");
       // openCamera();
        //Uncomment this to start capturing photo with delay of 2 second
       // startPhotoCapture(); // Calling the method to capture photo
        scheduleSurveillanceWorker();
    }

    private void startPhotoCapture(){
        if (!isCapturing){  // Ensure only one capture process is active at a time
            isCapturing=true;
            takePhoto();
        }
    }

    private void takePhoto(){
        new android.os.Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                if(isCapturing){
                    openCamera();
                    takePhoto();
                    Log.d(TAG, "Capturing Image After 2 sec Delay");
                }
            }
        },2000);
    }

    @Override
    protected void onPause(){
        super.onPause();
        vibrationDetector.stop();
    }

    protected void onResume(){
        super.onResume();
        vibrationDetector.start();
    }

    // Method to retrieve last known location
    private Location getLastKnownLocation(){
        LocationManager locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        // Check if permission is granted
        if (ActivityCompat.checkSelfPermission
                (this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED &&
                ActivityCompat.checkSelfPermission
                        (this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // Handle case where permission is not granted
            return null;
        }
        // Get last known location from providers
        Location lastKnownLocation = null;
        if (locationManager != null) {
            // Get GPS location
            lastKnownLocation = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            if (lastKnownLocation == null) {
                // Get network location if GPS is not available
                lastKnownLocation = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
            }
        }
        return lastKnownLocation;
    }


    private void scheduleSurveillanceWorker(){
        OneTimeWorkRequest workRequest = new OneTimeWorkRequest.Builder(SurveillanceWorker.class).build();
        WorkManager.getInstance(this).enqueue(workRequest);
    }

}
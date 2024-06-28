package com.capstone.hrushi.thirdeyesurveillance;

import android.content.Context;
import android.graphics.Bitmap;
import android.location.Location;
import android.os.Environment;

import androidx.annotation.NonNull;
import androidx.work.Worker;
import androidx.work.WorkerParameters;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class SurveillanceWorker extends Worker {

    public SurveillanceWorker(@NonNull Context context, @NonNull WorkerParameters params) {
        super(context, params);
    }

    @NonNull
    @Override
    public Result doWork() {

        // This could include checking for vibrations, capturing images, etc.

        // Example: Capture an image and save it with location data
        Location currentLocation = getLastKnownLocation();
        try {

            Bitmap imageBitmap = captureImage();
            StorageHelper.saveCompressedImage(getApplicationContext(), imageBitmap, currentLocation);
        } catch (IOException e) {
            e.printStackTrace();
            return Result.failure();
        }

        return Result.success();
    }

    private Location getLastKnownLocation() {
        return null;
    }

    private Bitmap captureImage() {
        return null;
    }

    private void saveCompressedImage(Context context, Bitmap bitmap, Location location) throws IOException {
        File storageDir = context.getExternalFilesDir(Environment.DIRECTORY_PICTURES);
        if (!storageDir.exists() && !storageDir.mkdirs()) {
            throw new IOException("Failed to create directory");
        }

        String fileName = "IMG_" + System.currentTimeMillis() + ".jpg";
        File imageFile = new File(storageDir, fileName);

        try (FileOutputStream fos = new FileOutputStream(imageFile)) {
            if (!bitmap.compress(Bitmap.CompressFormat.JPEG, 85, fos)) {
                throw new IOException("Failed to compress image");
            }
        }

    }
}

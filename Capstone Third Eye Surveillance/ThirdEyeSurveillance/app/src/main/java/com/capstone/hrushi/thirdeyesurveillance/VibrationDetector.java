package com.capstone.hrushi.thirdeyesurveillance;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Handler;
import android.util.Log;

public class VibrationDetector implements SensorEventListener {
    private static final String TAG = "VibrationDetector";
    private static final float VIBRATION_THRESHOLD = 2.0f; // Adjust threshold as needed
    private static final int VIBRATION_DELAY = 2000; // 2 seconds delay between checks
    private SensorManager sensorManager;
    private Sensor accelerometer;
    private VibrationListener listener;
    private boolean isVibrating = false;
    private Handler handler = new Handler();

    public interface VibrationListener {
        void onVibrationDetected();
    }

    public VibrationDetector(Context context, VibrationListener listener) {
        this.listener = listener;
        sensorManager = (SensorManager) context.getSystemService(Context.SENSOR_SERVICE);
        if (sensorManager != null) {
            accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        }
    }

    public void start() {
        if (accelerometer != null) {
            sensorManager.registerListener(this, accelerometer, SensorManager.SENSOR_DELAY_NORMAL);
            Log.d(TAG, "Accelerator Sensor Available");
        } else {
            Log.e(TAG, "Accelerometer sensor not available");
        }
    }

    public void stop() {
        if (sensorManager != null) {
            sensorManager.unregisterListener(this);
        }
        handler.removeCallbacksAndMessages(null);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if (event.sensor.getType() == Sensor.TYPE_ACCELEROMETER) {
            float x = event.values[0];
            float y = event.values[1];
            float z = event.values[2];

            // Calculate acceleration magnitude
            float acceleration = (float) Math.sqrt(x * x + y * y + z * z);
            if (acceleration > VIBRATION_THRESHOLD) {
                if (!isVibrating) {
                    isVibrating = true;
                    startVibrationHandler();
                }
            } else {
                isVibrating = false;
                handler.removeCallbacksAndMessages(null);
            }
        }
    }

    private void startVibrationHandler() {
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                if (isVibrating && listener != null) {
                    listener.onVibrationDetected();
                    startVibrationHandler(); // Re-run the handler
                }
            }
        }, VIBRATION_DELAY);
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        // No need to handle accuracy changes for this scenario
    }
}
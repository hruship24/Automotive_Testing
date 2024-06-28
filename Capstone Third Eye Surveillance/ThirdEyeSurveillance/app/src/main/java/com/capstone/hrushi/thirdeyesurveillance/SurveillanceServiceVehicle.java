package com.capstone.hrushi.thirdeyesurveillance;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public abstract class SurveillanceServiceVehicle extends Service {


    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        // Start monitoring the vehicle status
        monitorVehicleStatus();
        return START_STICKY; // Ensures service is restarted if terminated
    }
    @Override
    public IBinder onBind(Intent intent) {
        return null; // Not binding to any client
    }
    @Override
    public void onDestroy() {
        super.onDestroy();
        // Clean up any resources when the service is destroyed
        stopMonitoringVehicleStatus();
    }

    protected abstract void stopMonitoringVehicleStatus();

    private void monitorVehicleStatus() {
        // Simulated methods to check vehicle status
        boolean isVehicleLocked = checkIfVehicleIsLocked();
        boolean isEngineOff = checkIfEngineIsOff();

        if (isVehicleLocked && isEngineOff) {
            startSurveillance();
        } else {
            stopSurveillance();
        }
    }

    private void startSurveillance() {
        // Logic to start the surveillance system
        Log.d("SurveillanceService", "Surveillance started");
        // Code to initiate camera capture, image storage, etc
    }

    private void stopSurveillance() {
        // Logic to stop the surveillance system
        Log.d("SurveillanceService", "Surveillance stopped");
        // Code to stop camera capture, image storage, etc
    }


    private boolean checkIfVehicleIsLocked() {
        // Implement actual logic to check if the vehicle is locked
        return true; // Placeholder
    }

    private boolean checkIfEngineIsOff() {
        // Implement actual logic to check if the engine is off
        return true; // Placeholder
    }

    @Override
    public void onCreate() {
        super.onCreate();
        // Initialize any resources needed for the service
    }


}
class VehicleEventReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        // Start the SurveillanceService when the vehicle is locked and engine is off
        Intent serviceIntent = new Intent(context, SurveillanceServiceVehicle.class);
        context.startService(serviceIntent);
    }


}



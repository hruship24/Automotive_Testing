package demo;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;

public class ApkInstall {

	public static void main(String[] args) throws MalformedURLException, InterruptedException {
		// Gather desired Capabilities

		DesiredCapabilities capabilities = new DesiredCapabilities();

		capabilities.setCapability("platformName", "Android");
		capabilities.setCapability("appium:deviceName", "emulator-5556");
		capabilities.setCapability("appium:app", "C:\\Users\\Administrator\\Desktop\\Appium Testing\\VirtualDevice\\Apk Downloadable files\\edx.apk");
		capabilities.setCapability("appium:automationName", "UiAutomator2");
		capabilities.setCapability("appium:appActivity", "org.edx.mobile.view.SplashActivity");
		capabilities.setCapability("appium:appPackage", "org.edx.mobile");
		
		URL url= URI.create("http://127.0.0.1:4723/wd/hub").toURL();
		AndroidDriver driver=new AndroidDriver(url, capabilities);
		
		
		System.out.println("Application Started ....");
		Thread.sleep(6000);
		driver.quit();
		System.out.println("Application Stopped.!");

	}

}

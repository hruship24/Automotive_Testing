package demo;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.AppiumBy;

public class HandleTextBoxCheckBoxRadioBtn {

	public static void main(String[] args) throws MalformedURLException, InterruptedException {
		// TODO Auto-generated method stub

		// Gather desired Capabilities

		DesiredCapabilities capabilities = new DesiredCapabilities();

		capabilities.setCapability("platformName", "Android");
		capabilities.setCapability("appium:deviceName", "emulator-5556");
		capabilities.setCapability("appium:automationName", "UiAutomator2");
		capabilities.setCapability("appium:appActivity", "io.appium.android.apis.ApiDemos");
		capabilities.setCapability("appium:appPackage", "io.appium.android.apis");

		URL url = URI.create("http://127.0.0.1:4723/wd/hub").toURL();
		AndroidDriver driver = new AndroidDriver(url, capabilities);

		System.out.println("Application Started");

		Thread.sleep(5000);

		// Scroll to "Views"
		driver.findElement(AppiumBy.androidUIAutomator(
				"new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView(\"Views\");"));

		// Click on views button using resourceId

		WebElement views = driver.findElements(By.id("android:id/text1")).get(10);
		views.click();

		Thread.sleep(3000);

		// Click on controls button using resourceId

		WebElement controls = driver.findElements(By.id("android:id/text1")).get(4);
		controls.click();

		Thread.sleep(3000);

		// Click on Light Theme button using resourceId

		WebElement lightTheme = driver.findElements(By.id("android:id/text1")).get(0);
		lightTheme.click();

		Thread.sleep(3000);

		// Enter Text here

		driver.findElement(By.id("io.appium.android.apis:id/edit")).sendKeys("Hrushi");

		// Check 1st check box

		driver.findElement(By.id("io.appium.android.apis:id/check1")).click();

		// Click on 2nd Radio button

		driver.findElement(By.id("io.appium.android.apis:id/radio2")).click();

		driver.quit();
		System.out.println("Applicated Stopped");

	}

}

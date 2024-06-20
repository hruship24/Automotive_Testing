package demo;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;

public class AutomateCalc {

	public static void main(String[] args) throws MalformedURLException, InterruptedException {
		// TODO Auto-generated method stub
		
		// Gather desired Capabilities
		
		DesiredCapabilities capabilities = new DesiredCapabilities();

		capabilities.setCapability("platformName", "Android");
		capabilities.setCapability("appium:deviceName", "emulator-5556");
		capabilities.setCapability("appium:automationName", "UiAutomator2");
		capabilities.setCapability("appium:appActivity", "com.android.calculator2.Calculator");
		capabilities.setCapability("appium:appPackage", "com.android.calculator2");
		
		URL url= URI.create("http://127.0.0.1:4723/wd/hub").toURL();
		AndroidDriver driver=new AndroidDriver(url, capabilities);
		
		// Click on number 8 using resourceId
		
		WebElement num8= driver.findElement(By.id("com.android.calculator2:id/digit_8"));
		num8.click();
		
		// Click on plus sign button using resourceId
		
		WebElement plusSign= driver.findElement(By.id("com.android.calculator2:id/op_add"));
		plusSign.click();
		
		// Click on number 2 using resourceId
		WebElement num2= driver.findElement(By.id("com.android.calculator2:id/digit_2"));
		num2.click();
		
		
		// Click on equal "=" sign button using resourceId
		WebElement equalSign= driver.findElement(By.id("com.android.calculator2:id/eq"));
		equalSign.click();
		
		
		// Capture and verify the result of the addition
		WebElement result= driver.findElement(By.id("com.android.calculator2:id/result"));
		String additionResult=result.getText();
		
		
		
		System.out.println("Application Started ....");
		
		if(additionResult.equals("10")) {
			System.out.println("Pass");
		}else {
			System.out.println("Fail");
		}
		
		Thread.sleep(6000);
		driver.quit();
		System.out.println("Application Stopped.!");

	}

}

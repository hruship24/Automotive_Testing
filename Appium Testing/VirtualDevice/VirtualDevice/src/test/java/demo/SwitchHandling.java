package demo;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;

public class SwitchHandling {

	public static void main(String[] args) throws MalformedURLException, InterruptedException {
		// TODO Auto-generated method stub
		
		// Gather desired Capabilities
		
		DesiredCapabilities capabilities = new DesiredCapabilities();

		capabilities.setCapability("platformName", "Android");
		capabilities.setCapability("appium:deviceName", "emulator-5556");
		capabilities.setCapability("appium:automationName", "UiAutomator2");
		capabilities.setCapability("appium:appActivity", "io.appium.android.apis.ApiDemos");
		capabilities.setCapability("appium:appPackage", "io.appium.android.apis");
		
		URL url= URI.create("http://127.0.0.1:4723/wd/hub").toURL();
		AndroidDriver driver=new AndroidDriver(url, capabilities);
		
		System.out.println("Application Started");
		
		// Scroll to "Views"
        driver.findElement(AppiumBy.androidUIAutomator("new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView(\"Views\");"));
		
        
		// Click on views button using resourceId
		
		WebElement views= driver.findElements(By.id("android:id/text1")).get(10);
		views.click();

			
		// Switch the "Monitored Switch" button on
		String scroll= "Switches";
		
		WebElement switchElement= driver.findElement(AppiumBy.androidUIAutomator("new UiScrollable(new UiSelector().scrollable(true))"+".scrollIntoView(new UiSelector().text(\""+scroll+"\"))"));
	
		switchElement.click();
		

        Thread.sleep(3000);
		// Click on monitor switch using resourceId

		 driver.findElement(By.xpath("//android.widget.Switch[@content-desc=\"Monitored switch\"]")).click();
	
		 
		 System.out.println("Action has been performed and the switch is ON now!");
		 
		
		Thread.sleep(3000);
		
		// Quit the session
		
		driver.quit();
		System.out.println("Application Ended!");
		
		
		
	
	}

}

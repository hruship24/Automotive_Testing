package demo;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.android.AndroidDriver;

public class AutomateDialer {

	public static void main(String[] args) throws MalformedURLException, InterruptedException {
		// TODO Auto-generated method stub
		
		// Gather desired Capabilities
		
				DesiredCapabilities capabilities = new DesiredCapabilities();

				capabilities.setCapability("platformName", "Android");
				capabilities.setCapability("appium:deviceName", "emulator-5556");
				capabilities.setCapability("appium:automationName", "UiAutomator2");
				capabilities.setCapability("appium:appActivity", "com.android.dialer.DialtactsActivity");
				capabilities.setCapability("appium:appPackage", "com.android.dialer");
				
				URL url= URI.create("http://127.0.0.1:4723/wd/hub").toURL();
				AndroidDriver driver=new AndroidDriver(url, capabilities);
				
				System.out.println("Application Started");
				System.out.println("Dialling number....");


				// Click to open dialer using resourceId
				
				WebElement openDialer= driver.findElement(By.id("com.android.dialer:id/floating_action_button"));
				openDialer.click();
				
				Thread.sleep(5000);
				
				// Click on number 9 using resourceId
				
				WebElement num9= driver.findElement(By.id("com.android.dialer:id/nine"));
				num9.click();
				
				
				// Click on number 5 using resourceId
				WebElement num5= driver.findElement(By.id("com.android.dialer:id/five"));
				num5.click();
				
				
				// Click on number 2 using resourceId
				WebElement num2= driver.findElement(By.id("com.android.dialer:id/two"));
				num2.click();
				
				// Click on number 7 using resourceId
				WebElement num7= driver.findElement(By.id("com.android.dialer:id/seven"));
				num7.click();
				
				// Click on number 0 using resourceId
				WebElement num0= driver.findElement(By.id("com.android.dialer:id/zero"));
				num0.click();
				
				// Click on number 8 using resourceId
				WebElement num8= driver.findElement(By.id("com.android.dialer:id/eight"));
				num8.click();
				
				// Click on number 2 using resourceId
				num2.click();
				
				// Click on number 6 using resourceId
				WebElement num6= driver.findElement(By.id("com.android.dialer:id/six"));
				num6.click();
				
				// Click on number 9 using resourceId
				num9.click();
				
				// Click on number 4 using resourceId
				WebElement num4= driver.findElement(By.id("com.android.dialer:id/four"));
				num4.click();
				
				System.out.println("Calling.....");

				
				// Click on call button using resourceId
				WebElement callButton= driver.findElement(By.id("com.android.dialer:id/dialpad_floating_action_button"));
				callButton.click();
				
					
				
				Thread.sleep(6000);
				

				// Click on call end button using resourceId
				WebElement endCall= driver.findElement(By.id("com.android.dialer:id/floating_end_call_action_button"));
				endCall.click();
				
				System.out.println("Call Ended.!");
				
				
				
				driver.quit();
				System.out.println("Application Stopped.!");


	}

}

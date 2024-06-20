package demo;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;
import java.time.Duration;
import java.util.Arrays;

import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Pause;
import org.openqa.selenium.interactions.PointerInput;
import org.openqa.selenium.interactions.Sequence;
import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;

public class DragandDrop {

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
		
		
        Thread.sleep(3000);
		// Click on Drag and Drop button 
        
		driver.findElement(By.xpath("//android.widget.TextView[@content-desc=\"Drag and Drop\"]")).click();
		
		// Selecting the ball for drag and drop from source position and target position
		
		WebElement sourcePostion = driver.findElement(By.xpath("//android.view.View[@resource-id=\"io.appium.android.apis:id/drag_dot_1\"]"));
		
		WebElement targetPosition = driver.findElement(By.xpath("//android.view.View[@resource-id=\"io.appium.android.apis:id/drag_dot_2\"]"));
	
		// Find center of the source and target element
		
		Point sourPositionCenter = getCenter(sourcePostion);
		Point targetPositionCenter = getCenter(targetPosition);
		
		/* PointerInput class to create a sequence of actions that move the pointer to the center
		 * of the element 
		 * Press down on that element and then release the element at target position
		*/
		
		PointerInput touchAction = new PointerInput(PointerInput.Kind.TOUCH, "touchAction");
		
		Sequence sequence = new Sequence(touchAction, 1)
				
				// Touch action at the initial position
				.addAction(touchAction.createPointerMove(Duration.ZERO, PointerInput.Origin.viewport(), sourPositionCenter))
		
				// Touch action on screen
				.addAction(touchAction.createPointerDown(PointerInput.MouseButton.LEFT.asArg()))
				
				.addAction(new Pause(touchAction, Duration.ofMillis(600)))
				
				// Touch action to target position
				.addAction(touchAction.createPointerMove(Duration.ofMillis(600), PointerInput.Origin.viewport(), targetPositionCenter))
				
				// now move touch action from the action up / release from screen
				.addAction(touchAction.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));
		
		// Perform these sequence of actions for drag and drop
		System.out.println("Performing Drag and Drop sequence.......");
		driver.perform(Arrays.asList(sequence));
		
		Thread.sleep(3000);
		
		driver.quit();
		System.out.println("Session ended. Drag and Drop Performed!");
		
	}
	
	
	private static Point getCenter(WebElement ele) {
		
		// Getting the location of our web element 
		
		Point loc = ele.getLocation();
		
		
		// Getting the dimension i.e. height and width of the element
		
		Dimension dimension = ele.getSize();
		
		// Calculating the center of the element
		
		Point center = new Point(loc.x + dimension.width/2, loc.y + dimension.height/2);
		
		return center;
		
	}

}







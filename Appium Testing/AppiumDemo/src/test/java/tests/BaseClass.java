package tests;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;


import io.appium.java_client.android.AndroidDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class BaseClass extends ExtentReportDemo {
    
    AndroidDriver driver;
    
    @BeforeTest
    public void setup() throws MalformedURLException {
        // Use WebDriverManager to manage ChromeDriver
        WebDriverManager.chromedriver().setup();
        
        // Gather desired Capabilities
        DesiredCapabilities capabilities = new DesiredCapabilities();

        capabilities.setCapability("platformName", "Android");
        capabilities.setCapability("appium:deviceName", "emulator-5554");
        capabilities.setCapability("appium:automationName", "UiAutomator2");
        capabilities.setCapability("udid", "emulator-5554");
        capabilities.setCapability("platformVersion", "9.0");
        
        /* The number of seconds the appium server should wait for client
         * to send commands before deciding that the client has
         * gone away and the session should shut down */
        capabilities.setCapability("appium:newCommandTimeout", 600);
        
        capabilities.setCapability("browserName", "Chrome");
        
        URL url = URI.create("http://127.0.0.1:4723/wd/hub").toURL();
        driver = new AndroidDriver(url, capabilities);
        
        // Adding implicit wait
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }
    
    @Test
    public void sampleTest() {
        driver.get("https://www.google.com/");
        
        // Adding a sleep to observe the browser behavior (remove in actual tests)
        try {
            Thread.sleep(5000); // Sleep for 5 seconds
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        // Add any further test steps here (e.g., searching for a term)
    }
    
    @AfterTest
    public void tearDown() {
        if (driver != null) {
            driver.quit(); // Close the session
        }
    }
}

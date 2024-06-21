package tests;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.testng.annotations.Test;

import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;

import pages.GoogleSearchPage;


public class SearchTest extends BaseClass{
	
	@Test
	public void test1() throws InterruptedException {
		
		ExtentTest test1 = extent.createTest("Test1", "This is Demo test case");
		
		test1.log(Status.INFO, "Test1 has Started.");
		
		
		driver.get("https://www.google.com/");
		test1.log(Status.PASS, "Google URL opened.");

		System.out.println("Getting to google page...");
		
		//find search box web element
		WebElement searchBox = driver.findElement(By.name("q"));
		Thread.sleep(5000);
		System.out.println("typing in search box.....");
		searchBox.sendKeys("One Piece Anime");
		
		test1.log(Status.PASS, "Search data Entered.");

		
		searchBox.sendKeys(Keys.RETURN);
		
		test1.log(Status.PASS, "Enter key in search box is pressed.");
		
		Thread.sleep(5000);
	}
	
	@Test
	public void test2() throws InterruptedException {
		
		ExtentTest test2 = extent.createTest("Test2", "This is Demo test case");
		test2.log(Status.INFO, "Test2 has Started.");
		
		GoogleSearchPage gsp=new GoogleSearchPage(driver);
		driver.get("https://www.google.com");
		test2.log(Status.PASS, "Google URL opened.");

		
		gsp.EnterSearchData("Death Note Anime");
		test2.log(Status.PASS, "Search data Entered.");

		gsp.pressEnterKeyOnKeyboard();
		test2.log(Status.PASS, "Enter key in search box is pressed.");
		
		Thread.sleep(5000);
	}

}

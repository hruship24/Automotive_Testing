package tests;

import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;

public class ExtentReportDemo {
	
	ExtentReports extent;
	ExtentSparkReporter spark;
	
	@BeforeSuite
	public void setupReport() {
		
		extent = new ExtentReports();
	    spark = new ExtentSparkReporter("extent_report.html");
	    extent.attachReporter(spark);

		
	}
	
	@AfterSuite
	public void teardown() {
		extent.flush();
	}

}

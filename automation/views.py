from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    """Render the home page with automation UI"""
    return render(request, 'automation/home.html')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@csrf_exempt
def login_automation(request):
    """
    API endpoint to perform login automation
    Accepts POST request with optional email and password
    Returns JSON response with status and message
    """
    if request.method == 'POST':
        # Parse JSON body if present
        try:
            data = json.loads(request.body)
            email = data.get('email', 'swanim@yopmail.com')
            password = data.get('password', 'Test@123')
        except:
            # If JSON parsing fails, use default values
            email = 'swanim@yopmail.com'
            password = 'Test@123'
    else:
        # For GET requests, use default values
        email = request.GET.get('email', 'swanim@yopmail.com')
        password = request.GET.get('password', 'Test@123')
    
    driver = None
    try:
        # Initialize Chrome driver with automatic driver management
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://shivamjewelleryandtools.quickstockbill.com/login")
        driver.maximize_window()
        time.sleep(1)
        
        # Find and fill email field
        email_field = driver.find_element(By.XPATH, "//input[@type='text']")
        email_field.send_keys(email)
        
        # Find and fill password field
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")
        password_field.send_keys(password)
        
        # Click login button
        login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()
        
        # Alternative: submit using Enter key
        # password_field.send_keys(Keys.RETURN)
        
        time.sleep(3)
        
        # Navigate to customers page
        driver.get("https://shivamjewelleryandtools.quickstockbill.com/customers")
        time.sleep(3)
        
        # Check if login was successful (you can add more validation here)
        current_url = driver.current_url
        
        driver.quit()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Login automation completed successfully',
            'email': email,
            'redirected_to': current_url
        })
        
    except NoSuchElementException as e:
        if driver:
            driver.quit()
        return JsonResponse({
            'status': 'error',
            'message': f'Element not found: {str(e)}'
        }, status=400)
        
    except ElementClickInterceptedException as e:
        if driver:
            driver.quit()
        return JsonResponse({
            'status': 'error',
            'message': f'Element click intercepted: {str(e)}'
        }, status=400)
        
    except Exception as e:
        if driver:
            driver.quit()
        return JsonResponse({
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }, status=500)


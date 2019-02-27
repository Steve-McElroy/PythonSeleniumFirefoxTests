#! python 3

'''
Assumptions made;
1 - Colours of buttons do not change
2 - For the three coloured buttons (blue, red, green), the text displayed will only
    ever be "bar", "baz", "foo", "qux"
3 - The font used for the buttons is always inherited from the HTML
3 - Edit / delete buttons are not functional other than updating the URL
4 - The table of values (lorem, ipsum etc.) does not change and can be treated as static
'''

import unittest, os, pyautogui, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Geckodriver required for running FF
geckodriver = 'geckodriver.exe'

# URL of required site
url = 'https://the-internet.herokuapp.com/challenging_dom'

class ChallengingDom(unittest.TestCase):

	# Initialise required driver 
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = geckodriver)

    # Load URL and verify the title is as expected
    def test_01_Title(self):
        print('\n Running Test 1: Title')
        driver = self.driver
        driver.get(url)
        title = driver.find_element_by_css_selector('.example > h3:nth-child(1)')
        titleText = title.get_attribute('innerHTML')
        if titleText == 'Challenging DOM':
            print('Test 1 passed')
        else:
            print('Test 1 failed')

    # Load URL and verify the header is as expected
    def test_02_Header(self):
        print('\n Running Test 2: Header')
        driver = self.driver
        driver.get(url)
        header = driver.find_element_by_css_selector('.example > p:nth-child(2)')
        headerText = header.get_attribute('innerHTML')
        expectedText = r"The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element."
        if headerText == expectedText:
            print('Test 2 passed')
        else:
            print('Test 2 failed')

    # Locate the blue button and verify the text is one of 4 choices
    def test_03_Blue_Button_Text(self):
        print('\n Running Test 3: Blue Button Text')
        driver = self.driver
        driver.get(url)
        choices = {'bar' : 0, 'baz' : 0, 'foo' : 0, 'qux' : 0}
        i = 0
        while i < 5:
            blueButton = driver.find_element_by_class_name('button')
            blueButtonText = blueButton.get_attribute('innerHTML')
            assert(blueButtonText in ('bar','foo','baz', 'qux'))
            if blueButtonText == 'bar':
            	choices['bar'] = 1
            elif blueButtonText == 'baz':
            	choices['baz'] = 1
            elif blueButtonText == 'foo':
            	choices['foo'] = 1
            else:
            	choices['qux'] = 1
            i += 1
            choicesCovered = all(value == 1 for value in choices.values())
            if choicesCovered == True:
            	print('All possible values seen')
            else:
            	print('Still checking button text...')
            print('Text verified %d times And this time the button said %s.' % (i, blueButtonText))
            blueButton.click()

    # Locate the blue button and verify the background colour remains consistent
    def test_04_Blue_Button_BackgroundColour(self):
        print('\n Running Test 4: Background Colour')
        driver = self.driver
        driver.get(url)
        i = 0
        while i < 5:
            blueButton = driver.find_element_by_class_name('button')
            blueButtonColour = blueButton.value_of_css_property('background-color')
            assert(blueButtonColour == r'rgb(43, 166, 203)')
            i += 1
            print('Colour of HEX VALUE #2ba6cb translates to rgb(43, 166, 203). Seeb %d times as %s.' % (i, blueButtonColour))
            blueButton.click()

    def test_05_Blue_Button_Font(self):
        print('\n Running Test 5: Blue Button Font')
        driver = self.driver
        driver.get(url)
        i = 0
        while i < 5:
            blueButton = driver.find_element_by_class_name('button')
            blueButtonFont = blueButton.value_of_css_property('font-family')
            assert(blueButtonFont == r'"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif')
            i += 1
            print('Font verified %d times.' % i)
            blueButton.click()

    # Locate the red button and make some assertions
    def test_06_Red_Button_Text(self):
        print('\n Running Test 6: Locate Red Button')
        driver = self.driver
        driver.get(url)
        i = 0
        try:
            redButton = driver.find_element_by_class_name('button alert')
            redText = redButton.get_attribute('innerHTML')
            redColourCheck = redButton.value_of_css_property('background-color')
            assert('bar','foo','baz', 'qux') in redText
            assert(redColourCheck == r'rgb(198, 15, 19)')
            i += 1
            redButton.click()
        except NoSuchElementException:
            print("Could not find by class name")
        try:
            redButton = driver.find_element_by_id(r'36ec3210-1c2c-0137-5b6f-6621f150b69f')
            redText = redButton.get_attribute('innerHTML')
            redColourCheck = redButton.value_of_css_property('background-color')
            assert('bar','foo','baz', 'qux') in redText
            assert(redColourCheck == r'rgb(198, 15, 19)')
            i += 1
            redButton.click()
        except NoSuchElementException:
            print("Could not find by ID")
        try:
            redButton = driver.find_element_by_css_selector(r'#\33 6ec3210-1c2c-0137-5b6f-6621f150b69f')
            redText = redButton.get_attribute('innerHTML')
            redColourCheck = redButton.value_of_css_property('background-color')
            assert('bar','foo','baz', 'qux') in redText
            assert(redColourCheck == r'rgb(198, 15, 19)')
            i += 1
            redButton.click()
        except NoSuchElementException:
            print('Could not find by css selector')
        try:
            redButton = driver.find_element_by_xpath(r'//*[@id="c5b0cdb0-1376-0137-3365-1e74419702e1"]')
            redText = redButton.get_attribute('innerHTML')
            redColourCheck = redButton.value_of_css_property('background-color')
            assert('bar','foo','baz', 'qux') in redText
            assert(redColourCheck == r'rgb(198, 15, 19)')
            i += 1
            redButton.click()
        except NoSuchElementException:
            print('Could not find by Xpath')
        assert(i > 0)

    # Locate the green button and make some assertions
    def test_07_Green_Button(self):
        print('\n Running Test 7: Locate Green Button')
        driver = self.driver
        driver.get(url)
        i = 0
        try:
            greenButton = driver.find_element_by_class_name('button success')
            greenText = greenButton.get_attribute('innerHTML')
            assert('bar','foo','baz', 'qux') in greenText
            i += 1
        except NoSuchElementException:
            print('Could not find the green button by class name')
        assert(i > 0)

    def test_08_Answer_Panel_Height(self):
        print('\n Running Test 8: Verify Canvas Height')
        driver = self.driver
        driver.get(url)
        answerPanel = driver.find_element_by_id('canvas')
        answerPanelHeight = answerPanel.get_attribute('height')
        assert(answerPanelHeight == '200')
        print('%s observed. 200 expected' % answerPanelHeight)


    def test_09_Answer_Panel_Width(self):
        print('\n Running Test 9: Verify Canvas Width')
        driver = self.driver
        driver.get(url)
        answerPanel = driver.find_element_by_id('canvas')
        answerPanelWidth = answerPanel.get_attribute('width')
        assert(answerPanelWidth == '599')
        print('%s observed. 599 expected' % answerPanelWidth)

    def test_10_Answer_Panel_Border(self):
        print('\n Running Test 10: Verify Canvas Border Style')
        driver = self.driver
        driver.get(url)
        answerPanel = driver.find_element_by_id('canvas')
        answerPanelBorder = answerPanel.value_of_css_property('border-top-style')
        assert(answerPanelBorder == 'dotted')
        print('%s observed. Dotted expected' % answerPanelBorder)
        
    def test_11_Main_Table(self):
        print('\n Running Test 11: Verify Table Is Present')
        #os.chdir('X:\My Documents\Coding\Python_Scripts\Automate the Boring Stuff (Udemy Course)')
        tableReferenceImage = 'table_options_2.PNG'
        driver = self.driver
        driver.get(url)
        print('Waiting while image recognition is run...')
        time.sleep(5)
        tableCheck = pyautogui.onScreen(tableReferenceImage)
        if tableCheck == True:
            print('Image Found')
        else:
            print('Image not found or something else')
        assert(tableCheck == True)


    def test_12_external_url(self):
        print('\n Running Test 12: Verify External Url Is Functional')
        driver = self.driver
        driver.get(url)
        externalUrl = driver.find_element_by_css_selector('.large-4 > div:nth-child(2) > a:nth-child(1)')
        externalUrl.click()
        driver.switch_to.window(driver.window_handles[-1])
        currentUrl = driver.current_url
        assert(currentUrl == 'http://elementalselenium.com/')


    def test_13_GitHub_Link(self):
        print('\n Running Test 13: Verify GitHub Url Is Functional')
        driver = self.driver
        driver.get(url)
        gitHubLink = driver.find_element_by_css_selector('body > div:nth-child(2) > a:nth-child(1) > img:nth-child(1)')
        gitHubLink.click()
        driver.switch_to.window(driver.window_handles[-1])
        currentUrl = driver.current_url
        assert(currentUrl == 'https://github.com/tourdedave/the-internet')


    # Close browser after each test
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


from selenium import webdriver
import time

symbol_lists = ['AA', 'AAL', 'AAPL', 'ADI', 'AIG', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'APA', 'ASHR',
                'AVGO', 'BA', 'BABA', 'BHC', 'BIDU', 'BIIB', 'BP', 'BRK-B', 'BYND', 'CCAT', 'COF', 'COP', 'COST',
                'CRM', 'CRUS', 'CVX', 'DIA', 'DIS', 'EBAY', 'EEM', 'EWW', 'EWZ', 'FAS', 'FB', 'FCX', 'FSLR', 'FXE',
                'FXI', 'FXY', 'GBTC', 'GDX', 'GE', 'GILD', 'GLD', 'GM', 'GOOGL', 'GRMN', 'GS', 'HAL', 'HD', 'HES',
                'HYG', 'IBB', 'IBM', 'INTC', 'IWM', 'IYR', 'JD', 'JNJ', 'JPM', 'KLAC', 'LIN', 'LLY', 'LSCC', 'LYFT',
                'MCD', 'MDT', 'MMM', 'MRK', 'MRVL', 'MS', 'MSFT', 'MU', 'NFLX', 'NUGT', 'NVDA', 'OIH', 'OXY', 'PBR',
                'PCG', 'PFE', 'PFF', 'PG', 'PM', 'PXD', 'QCOM', 'QQQ', 'RIG', 'ROKU', 'SBUX', 'SFIX', 'SLB', 'SLV',
                'SMH', 'SOXX', 'SPLK', 'SPY', 'SQ', 'SRPT', 'STX', 'SVXY', 'TAN', 'TBT', 'TGT', 'TLT', 'TSLA', 'TSM',
                'TTWO', 'TWLO', 'TWTR', 'TXN', 'UBER', 'ULTA', 'USO', 'V', 'VXX', 'WB', 'WDAY', 'WDC', 'WFC', 'WMT',
                'WORK', 'WW', 'WYNN', 'X', 'XLE', 'XLF', 'XLU', 'XLV', 'XME', 'XOM', 'XOP', 'ZM']

def download(i, symbol, driver):
    # Initialize the setup with the correct timeframe and moving averge
    if i == 0:
        driver.get('https://finance.yahoo.com/chart/' + symbol)
        time.sleep(5)

        # Chart type button
        chart_button = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/div[6]')
        chart_button.click()
        time.sleep(0.5)
        # Candlebar Button
        candle_button = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/ul/li[3]/button')
        candle_button.click()
        time.sleep(0.5)

        # Indicator Button
        indicator_button = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div')
        indicator_button.click()
        time.sleep(0.5)
        # Moving Average Button
        mv_avg_button = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div[3]/div[2]/ul[1]/li[1]/button')
        mv_avg_button.click()
        time.sleep(0.5)        
        # Adjust period to 10-bar
        period_input = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div[2]/div/div/table/tbody/tr[1]/td[2]/input')
        period_input.clear()
        period_input.send_keys(10)
        # Color palette button
        color_btn = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div[2]/div/div/table/tbody/tr[5]/td[2]/div')
        color_btn.click()
        time.sleep(0.1)
        # Pick color blue
        blue_color_btn = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/ul/li[33]/button')
        blue_color_btn.click()
        time.sleep(0.1)
        # Save button
        save_btn = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div[2]/div/div/div[2]/button[1]')
        save_btn.click()

        # Indicator Button
        indicator_button = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div')
        indicator_button.click()
        time.sleep(0.5)
        # Moving Average Button
        mv_avg_button = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div[3]/div[2]/ul[1]/li[1]/button')
        mv_avg_button.click()
        time.sleep(0.5)        
        # Adjust period to 20-bar
        period_input = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div[2]/div/div/table/tbody/tr[1]/td[2]/input')
        period_input.clear()
        period_input.send_keys(20)
        # Color palette button
        color_btn = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div[2]/div/div/table/tbody/tr[5]/td[2]/div')
        color_btn.click()
        time.sleep(0.1)
        # Pick color yellow
        yellow_color_btn = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/ul/li[29]/button')
        yellow_color_btn.click()
        time.sleep(0.1)
        # Save button
        save_btn = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[1]/span[1]/div[2]/div/div/div[2]/button[1]')
        save_btn.click()
        time.sleep(0.2)

    # No need to reopen the page
    if i > 0:
        # Open the page
        driver.get('https://finance.yahoo.com/chart/' + symbol)
        time.sleep(5)

    # Click share button
    share_btn = driver.find_element_by_xpath('//*[@id="chart-toolbar"]/div[2]/div[2]/button')
    share_btn.click()
    time.sleep(3)
    # Click download button
    download_btn = driver.find_element_by_xpath('//*[@id="shareDialog"]/div/div/div/button[5]')
    download_btn.click()
    time.sleep(3)

if __name__ == "__main__":
    # load bot to control Chrome
    driver = None
    try:
        driver = webdriver.Chrome('./chromedriver')
    except:
        print("Server side error. Please make sure that selenium and chromedriver is installed \n. Also make sure that chromedriver is in the same folder as this Python script")
        quit()
    

    # download picture one by one
    for i in range(0, len(symbol_lists)):
        try:
            download(i, symbol_lists[i], driver)
        except:
            print("Something went wrong. Please try again in a few minutes. \nStart the for loop at index " + str(i))
            quit()
    
    driver.close()
    print('Done!')
    quit()
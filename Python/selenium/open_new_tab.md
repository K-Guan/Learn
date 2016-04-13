To open an empty tab in Python selenium, you can simply run the below code:

    driver.execute_script('window.open("about:blank", "_blank");')

Now, you opened a new tab, but however, if you try to run:

    driver.get('https://www.google.com/')

That doesn't work! I mean, selenium accessed the link in the fist tab, not the one you just opened!


It's because that selenium is still *using* the first tab. And you need *switch* to the tab you want to use.

`driver.switch_to_window()` can do it in this case. And all the tabs are just some `window_handles` in selenium:

    print(driver.window_handles)

`driver.window_handles` is a list which saves the id of every `window_handles`. The fist element in it is the first tab (index is `[0]`), sencond is the second (index is `[1]`), etc.

To switch to the **second tab** (I think it's the one you just opened - you can also change the index yourself otherwise), try the below code:

    driver.switch_to_window(driver.window_handles[1])

Do the stuff you want to do with that tab, once you want to close it and switch to the **first tab**, try:

    driver.close()  # closes the tab you're working on
    driver.switch_to_window(driver.window_handles[0])  # switchs to the first tab

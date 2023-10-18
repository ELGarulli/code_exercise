### Intro

Hi! Thank you for taking the time to chat today. Here is a tiny code exercise to conclude our interview. 
Please note that this is by no mean intended to test how much you know about coding. But rather, to see how you reason,
how you approach the code, and a bit of style-check.

### Made up context 

Let's suppose you have a bit of a weird device, it measures hourly changes in both humidity and temperature at the same time. So every hour the sensor registers how much the temperature has changed compared to the previous hour, same with the humidity.
The even values the sensor returns refer to changes in temperature, while the odd values refer to humidity (the sensor adapts the values so that all the temperature's values are even, and all the humidity's are odd). You are interested only in the temperature values (i.e., the even values), and you want to 
understand the total magnitude of fluctuations over the period the sensor was active.

The sensor returns a list of values, the temperature values are expressed in Celsius.

### Assignment

In the script main.py you can find a simple function to compute the total magnitude of fluctuations in temperature, 
in test_sum_ev.py you can find an example of a basic test. 

Please complete the following :
- think of at least one edge case that is not covered by the basic test and add a test for it
- is the function fully correct? Feel free to modify it
- there are many things to improve about the style of sum_ev, can you give it a little facelift?

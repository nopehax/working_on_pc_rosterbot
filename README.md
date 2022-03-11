# working_on_pc_rosterbot
Selenium python bot that helps to chope slots in the RMG e-roster
6_slots_per_week.py is for the new month; cos they won't allow you to book more than 6 slots. the script will book AM Monday to Saturday AM slots only.
eroster.py will just help to chope slots as they are released

Mr W. told us when they are gonna release the slots for July
So I ran the bot on the actual day and it didn't work.
The current code does not take into account loading time. There are so many people accessing the website all at once that the servers were overloaded. Then when the bot is selecting the vc centre, it returns no element found exception cos it hasn't loaded yet, causing the bot to stop.
The website even gave a 502 error at one point in time


# working_on_pc_rosterbot
Selenium python bot that helps to chope slots in the RMG e-roster
6_slots_per_week.py is for the new month; cos they won't allow you to book more than 6 slots. the script will book AM Monday to Saturday AM slots only.
eroster.py will just help to chope slots as they are released

so I ran the bot on the actual day when the slots are released and it didn't work.
so many people are accessing the website all at once that it took damn long to load. then when the bot is selecting the vc centre, it return no element found exception cos it hasn't loaded yet, causing the bot to stop

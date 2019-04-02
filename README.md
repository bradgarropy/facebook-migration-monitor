# 🆗 Facebook Migration Monitor

*During a recent phone interview with [Facebook][1], I was asked to complete a coding question in an online editor called [CoderPad][2]. I really enjoyed this question because it starts simple and can get increasingly complex as the interviewer changes assumptions and introduces constraints.*

## ❓ Question
Your company wants to migrate a service to a new port across all of the hosts that it's running on.  
Write a program that monitors the progress of this migration, and reports the status of migrated hosts.

The program should do the following:
* Determine if the service has been migrated on each host.
* Log the result of each host to the console.

It would be excellent if the program could also:
* Create output files listing hosts based on the status of the service.
    * Migrated successfully.
    * Not yet migrated.
    * Migrated but with errors.
* Log the monitor's estimated time remaining.
* Log the monitor's percent complete.
* Handle a large number of hosts.

## 🤔 Assumptions

The question gave no details regarding *how* to get the status of a service.

So in my implementation I wrote a `get_service_status(host, port)` method that mocks the functionality. I included a slight delay to simulate a network request, and randomized the result.

## 💀 Execution

If you want to see my solution, clone the repository and execute it locally!

```
git clone https://github.com/bradgarropy/facebook-migration-monitor.git
cd facebook-migration-monitor
python fmm.py 2000 3000 hosts.txt
```

[1]: https://www.facebook.com/careers
[2]: https://coderpad.io

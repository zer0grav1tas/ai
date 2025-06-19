# AI Automation Governance

## What is Governance and why you should care?

AI Governance is the processes by which an organization ensures that AI systems are being used effectively to achieve goals and minimize risks.

This is an all too often overlooked part of automation delivery, in a rush to implement a new process to improve or fix a business function critical tasks can be neglected or skipped entirely.

The delivery of good governance can be the difference between a business critical system working at the expected uptime and implementing a service that fails, does not do exactly what you expect it to do, or even worse introduces a serious security risk.

## Implementing Good Governance

When implementing any automation you should ask yourself the following questions:

1. Who are the key stakeholders for this task?
2. How am I going to document this solution?
3. Who is going to support the automation once it is live?
4. How is my automation going to connect to the resources that it is reading and writing from?
5. How am I going to ensure my automation is doing what it is supposed to be doing?
6. How am I going to control access to the automation?
7. How am I going to securely store my keys?

### Who are the key stakeholders for this task?

Understanding the key stakeholders for a process and ensuring that they sign off on the process before you begin can save hours of effort and frustration later when the work begins.

If work is started with no stakeholder involvement or the wrong stakeholders you will find that at some point someone will challenge what you are doing and how you are doing it, which could disrupt your entire strategy.

Your stakeholders are always:
- The person in the business who owns the processes you are affecting.
- Your compliance team, even if you think they are not needed, assume that they are.
- Security engineering, they will need to sign off your approach to security.

### How am I going to document this solution?

Documentation is critical to successful delivery, this will save you pain in the future. 12 months after you have delivered the automation, and 20 other tasks this one will fail. You will be trying to remember how it works and be regretting not documenting it, so do it before you launch and do it right.

- Before starting document what your automation is going to do.
- Include charts, charts are good, Mermaid charts are great, [Mermaid Charts](https://mermaid.live/edit#pako:eNpFjUsOgjAARK9CZo2E0g9tt3oK001jKxClJbUkKuHuIolxNy_zW3CJzkMDJbo0OOicZl9i9Gm0X8RiQlEY5N6P3kBv0tl0MzBh3TqTDecYx18txbnroa_2_thonpzN_jTYLtl_xAfn0zHOIUOLfQF6wRP6QFhVN0JIySmlUrCmLfGCppxXVCpGiWqZIozRtcR7fyUVIQ3nSrSCtDXd3PUDOw49yw). Having a visual guide to show the logic flow of a process can help to quickly understand a process and as a troubleshooting aid to understand where a failure occurred.
- Document everything:
  - What accounts are used.
  - What permissions each account has and where.
  - Where and how the secrets or passwords for the accounts are managed.
  - Who the stakeholders are.
  - Who to contact if things go wrong.
  - What every stage of the automation does.
  - What could go wrong and what to do if it does.

### Who is going to support the automation once it is live?

Generally speaking automation is created by a separate team to the support team. This is to ensure that the automation team is not tied down by support once a product is put into production.

Part of delivering an automation task into production is to handover to support. How something is handed over to support is different for each organization however these are some basic guidelines:

- Face to Face handover is always best, but not always possible when there is a high rate of change.
- Documentation should be detailed and include handover and authentication points in the automation process as these are the most likely points of failure.
- A support matrix should be supplied, this shows who is responsible for what aspect of the automation and who to escalate to if something goes wrong.

| Task | First Contact | Second Contact | Escalation |
|------|---------------|----------------|------------|
| Automation job failed to start | Service Desk | Tech Support | Automation Team |
| Automation tool showing license error | Service Desk | Vendor | N/A |

### How is my automation going to connect to the resources that it is reading and writing from?

When creating any automation task that needs to retrieve data or write data what often happens is too much access is granted.

This can happen for various reasons, sometimes because automation is migrated from a test environment where overly permissive permissions are used, the reuse of an existing SPN or account, or just because it was not considered.

When defining permissions for an automation task the following rules should be followed:

- **Create credentials for each task, DO NOT reuse credentials** - It can be tempting to say to yourself "This automation is accessing the same thing as that other automation so I can use the same account."; but what happens when one of the automation tasks is changed and the permissions need to be updated? You will very quickly end up with automations that have permissions that they do not need, or have permissions taken away that they need. This approach can lead to issues where a small change can break lots of automation tasks or even worse create a serious security risk.

- **Use the minimum required permissions** - This means ensuring that your accounts can only access what they need to access. e.g. If your automation only needs to read some files, ensure that it cannot read the whole file store. It has been said before but giving a process more access than it needs can cause security concerns but there is also a chance that an error in your code could have unintended consequences if the permissions are too broad.

- **Set an expiration date** - The credential secret or certificate should be cycled on a regular basis, never longer than 12 months, and definitely never set to never expire.

### How am I going to ensure my automation is doing what it is supposed to be doing?

When deploying automation you need to be able to check that it is doing what you want it to be doing at all times; you never want to be asked if it is working, or working correctly.

There are several ways to do this, including but not exclusive to:

- **Monitoring** - Create tools that check the output of your automation at different stages.

**Example:** You have an automation task to read data from a load of .csv files and import the data into a SharePoint list.

- Have checks to confirm that the number of csv files in the source matches the number of csv files processed.
- Validate that the data in the SharePoint list matches the data in the csv files.
- Validate that the number of rows created in SharePoint matches the number of rows in the csv files.
- Confirm that the job completed with no errors.

### How am I going to control access to the automation?

A lot of tech teams and security teams are great at ensuring that automation tasks can only do what they need to do with minimal permissions but they often forget about securing the automation task itself.

Your automation task may be restricted in what it can do, but could a malicious actor access the automation task itself and make changes that have a negative impact?

e.g. You have an automation task that analyzes sensitive information and creates summaries in a secure space. If someone had access to the automation could they redirect this output somewhere else, or even access the source data by manipulating the automation into surfacing it.

Securing the automation task is just as important as securing the tasks that the automation can do. So lock down your admin consoles, and git repos to just those that should have access to that specific automation task.

Add approvals for anyone wanting to edit an automation task. Making it hard to make changes might sound frustrating but it could save you a lot of pain in the future.

### How am I going to securely store my keys?

You will have to create keys, passwords or certificates for your automation to run, there is no way it runs under a user identity right?

These keys, passwords and certificates should be stored in a secure location that has restricted access and auditing, e.g. Azure KeyVault.

## Conclusion

Implementing governance for automation can seem like a lot of work, and it is, but the reward it provides for your future and the future of the organization cannot be overstated.

Good governance improves security, and supportability and ensures that automation is delivered to a high standard.

Do not look at governance as a barrier to delivery, look at it as giving your future self a gift.

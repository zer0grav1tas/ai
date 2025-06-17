# Simple Prompt Engineering Example Using Claude and CoPilot

## What is prompt engineering?

A prompt is the text you type in to the AI, or send via API, when you ask it to complete an action.

Prompt engineering is a process where you provide instructions to generative AI to ensure high quality output. This is done by providing clear instructions, context, examples, phrases and words that guide the AI to provide the desired output.

## Claude AI

**Scenario:** I want to process a list of service desk tickets to understand the most common issues.

**Data:**
```csv
TicketNumber,Description
123456,My laptop screen will not turn on.
123457,My laptop will not turn on.
123458,I cannot open Outlook.
123459,I am not getting any emails.
123460,I cannot connect to WiFI
123461,I have no network connectivity.
123462,I cannot get on the internet.
123463,My laptop battery dies quickly.
123464,I have lost my RSA token
123465,How do I claim expenses
123466,I cannot connect to the printer
```

### Initial prompt
> "Can you review the attached document and provide the most common issues?"

### Response
Based on my analysis of the 11 tickets in your dataset, here are the most common issues:

**Top Issues (Tied for #1)**

1. **Hardware/Power Issues** (3 tickets - 27%)
   - Laptop screen not turning on
   - Laptop not turning on at all
   - Laptop battery dying quickly

2. **Network/Connectivity Issues** (3 tickets - 27%)
   - WiFi connection problems
   - General network connectivity issues
   - Internet access problems

**Secondary Issues**

3. **Email/Outlook Issues** (2 tickets - 18%)
   - Cannot open Outlook application
   - Not receiving emails

**Less Common Issues** (1 ticket each)
- Security/Token Issues: Lost RSA token
- Administrative/Process Issues: Expense claim procedures
- Printer Issues: Cannot connect to printer

**Key Insights**

The data shows that hardware/power problems and network connectivity issues are equally prevalent, together accounting for 55% of all tickets. This suggests your IT support should prioritize having solutions ready for laptop power issues and network troubleshooting.

Email-related problems represent the third most common category, which combined with network issues, indicates that communication and connectivity are major pain points for users.

---

### Improved Prompt: Clear, Contextual, Specific, with Examples and giving the AI a role

> "Your task is to analyse IT Service Desk tickets in the attached file, highlight the most common issues and generate a report.
>
> Instructions:
> 1. Review only the description field.
> 2. Categorize the issues, for example "Networking", "Hardware", "Windows", "Linux", "Office", the output does not need to include these examples.
> 3. Group the issues by category
> 4. Output only the categories, and the percentage for each with the most common first and the least common last. The output should be bulleted by category. Do not include any summary information."

### Response
- Hardware: 36.4%
- Networking: 27.3%
- Email: 18.2%
- Security: 9.1%
- Administrative: 9.1%

---

## Copilot

The effect of prompt engineering is even more visible when using Copilot, it provides a more literal response than Claude by doing a word count rather than recognising the CSV as separate lines to be processed.

### Initial prompt
> "Can you review the attached document and provide the most common issues?"

### Response
Here's a summary of the most common issues reported in the ticket descriptions, based on keyword frequency:

🔍 **Most Common Keywords in Issues**

| Keyword | Frequency |
|---------|-----------|
| i       | 8         |
| my      | 4         |
| cannot  | 4         |
| laptop  | 3         |
| not     | 3         |
| on      | 3         |
| will    | 2         |
| turn    | 2         |
| connect | 2         |
| to      | 2         |

🧩 **Interpreted Common Issue Categories**

Based on these keywords and the original descriptions, the most common issue categories appear to be:

- Laptop Power Issues – e.g., "My laptop will not turn on"
- Connectivity Problems – e.g., "I cannot connect to WiFi", "I have no network connectivity"
- Email/Outlook Issues – e.g., "I cannot open Outlook", "I am not getting any emails"
- Peripheral Access – e.g., "I cannot connect to the printer"
- Battery Problems – e.g., "My laptop battery dies quickly"
- Lost Items – e.g., "I have lost my RSA token"
- General Queries – e.g., "How do I claim expenses"

Would you like a visual summary (like a bar chart or word cloud) of these issues?

### Improved Prompt: Clear, Contextual, Specific, with Examples and giving the AI a role

> "Your task is to analyse IT Service Desk tickets in the attached file, highlight the most common issues and generate a report.
>
> Instructions:
> 1. Review only the description field.
> 2. Categorize the issues, for example "Networking", "Hardware", "Windows", "Linux", "Office", the output does not need to include these examples.
> 3. Group the issues by category
> 4. Output only the categories, and the percentage for each with the most common first and the least common last. The output should be bulleted by category. Do not include any summary information."

### Response
- Hardware: 27.27%
- Other: 27.27%
- Networking: 18.18%
- Office Software: 9.09%
- Operating System: 9.09%
- Peripheral: 9.09%

---

## Summary

When Claude processed the initial prompt it did not categorize all tickets instead it created a 'Less Common Issues' bucket and it provided examples.

- **Hardware/Power Issues** (3 tickets - 27%)
- **Network/Connectivity Issues** (3 tickets - 27%)
- **Email/Outlook Issues** (2 tickets - 18%)
- **Less Common Issues** (1 ticket each)

When the prompt was improved and specifically asked for categorization and defined an output format, all tickets were categorized and the data was provided in a more concise format as requested. This makes the data easy to review and understand where the common issues are. The example business needs to understand why they are having so many hardware issues and need to get the Network team to review the infrastructure.

- Hardware: 36.4%
- Networking: 27.3%
- Email: 18.2%
- Security: 9.1%
- Administrative: 9.1%

Copilot's first run is understandable, I did not give it any instruction that told it not to do a word count, so its decision to do so is not wrong. By providing a more detailed prompt Copilot was able to provide a very good result and whilst there are differences between the Copilot and Claude output both are valid and provide insight into the data. With some further prompt changes these outputs could easily be made the same, for example we could specify exactly the categories we want to use and ask the AI to use a weighting for certain events e.g. "Treat anything that seems to be network related as a network issue even if it appears to be hardware."

- Hardware: 27.27%
- Other: 27.27%
- Networking: 18.18%
- Office Software: 9.09%
- Operating System: 9.09%
- Peripheral: 9.09%

Spending time crafting your prompt can drastically affect the outcome. AI systems work probabilistically and benefit from clear, specific instructions.

When using AI for business processes and automation getting the prompts right can drastically impact the results you get. My advice is that you should spend as much time as needed getting the prompts right and don't treat it like a minor part of the automation task, it is likely the most critical.

Anthropic have a great article on prompt engineering, it is a short read but will change how you interact with AI.
[Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

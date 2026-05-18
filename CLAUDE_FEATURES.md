e# Claude Features Learning Guide

A hands-on reference for exploring what Claude can do — work through it top to bottom, or jump to whatever interests you most. Check off experiments as you complete them.

---

## Conversation

### Basic Q&A
Claude answers questions in natural language. You can ask anything from factual lookups to opinions and explanations.

> **Try this:** Ask "Explain recursion like I'm 10 years old" and then follow up with "Now explain it like I'm a computer science student."

### Follow-up and Context
Claude remembers what you said earlier in the same conversation and can build on it.

> **Try this:** Tell Claude "I'm building a to-do app in Python." Then in the next message ask "What data structure should I use?" — without re-explaining the context.

### Tone and Style Control
You can ask Claude to adjust how it writes — formal, casual, concise, detailed, etc.

> **Try this:** Ask Claude to explain how the internet works. Then ask it to rewrite the same explanation as a tweet, then as a bedtime story.

### Role and Persona
You can ask Claude to take on a specific role or perspective to shape its answers.

> **Try this:** Say "Act as a skeptical senior engineer reviewing my code decisions" and describe a technical choice you made recently.

### Iterative Refinement
You can ask Claude to revise its own output — make it shorter, change the format, fix something specific.

> **Try this:** Ask Claude to write a bio for you. Then say "Make it 50% shorter and more casual."

---

## Code

### Code Generation
Claude can write code in almost any language from a plain-English description.

> **Try this:** Ask "Write a Python function that takes a list of numbers and returns only the even ones, with a docstring and a usage example."

### Code Explanation
Claude can walk through code line by line and explain what it does.

> **Try this:** Paste your `factorial.py` into a message and ask "Explain what each line does as if I've never seen Python before."

### Debugging
Claude can find bugs in code you share with it.

> **Try this:** Introduce a deliberate bug into one of your scripts (e.g. use `=` instead of `==` in a condition), paste it, and ask "What's wrong with this code?"

### Code Review
Claude can critique code for style, readability, and best practices.

> **Try this:** Paste `sum.py` and ask "Review this for readability and suggest improvements following PEP 8."

### Unit Test Generation
Claude can write tests for existing functions automatically.

> **Try this:** Paste your `factorial` function and ask "Write pytest unit tests for this, including edge cases like 0, 1, and negative numbers."

### Refactoring
Claude can restructure code to be cleaner without changing what it does.

> **Try this:** Ask "Refactor this code to be more Pythonic" and paste a few lines with explicit loops that could be list comprehensions.

### Language Translation
Claude can rewrite code from one language to another.

> **Try this:** Ask Claude to rewrite `sum.py` in JavaScript, then in Go.

---

## Files and Documents

### Summarization
Claude can read a document you paste and summarize it at any length.

> **Try this:** Paste the content of your `README.md` and ask "Summarize this in one sentence, then in one paragraph."

### Information Extraction
Claude can pull out specific data from unstructured text.

> **Try this:** Paste a few paragraphs of any article and ask "List every tool, technology, or programming language mentioned."

### Document Q&A
Claude can answer questions about a document without you re-reading it.

> **Try this:** Paste the content of `CLAUDE.md` and ask "What commands can I use to run scripts in this project?"

### Format Conversion
Claude can convert content between formats — plain text, Markdown, JSON, CSV, HTML, etc.

> **Try this:** Write a short list of your three favorite movies with a one-line description of each. Then ask Claude to convert it to a JSON array with `title` and `description` fields.

### Template Generation
Claude can create reusable templates for documents, emails, reports, etc.

> **Try this:** Ask "Create a Markdown template for a weekly dev log — sections for what I built, what I learned, and blockers."

---

## Writing and Editing

### Drafting
Claude can write first drafts of anything — emails, docs, commit messages, READMEs.

> **Try this:** Describe a small feature you added to a project and ask Claude to write the git commit message and a one-paragraph section for a README.

### Proofreading
Claude can catch grammar, clarity, and tone issues in writing.

> **Try this:** Write a short paragraph intentionally with a few errors and vague sentences. Ask "Proofread this and explain each change you made."

### Rewriting for Audience
Claude can rewrite the same content for different audiences.

> **Try this:** Ask Claude to explain what a REST API is. Then say "Rewrite that for a non-technical product manager."

---

## Reasoning and Analysis

### Step-by-Step Problem Solving
Claude can break complex problems into steps and think through them out loud.

> **Try this:** Ask "I need to add user authentication to my Python app. Walk me through the key decisions I need to make, step by step."

### Pros and Cons Analysis
Claude can evaluate options and lay out trade-offs.

> **Try this:** Ask "What are the pros and cons of using a SQL database vs. a NoSQL database for a simple to-do app?"

### Decision Support
Claude can help you think through a decision by asking clarifying questions or presenting a framework.

> **Try this:** Say "Help me decide whether to learn FastAPI or Django next. Ask me questions to figure out which fits my goals better."

### Hypothesis Generation
Claude can brainstorm possible explanations for a problem.

> **Try this:** Describe a bug you've seen — "My script works when I run it manually but fails in CI" — and ask "What are five possible reasons for this?"

---

## Structured Output

### Lists and Tables
Claude can organize information into structured formats on request.

> **Try this:** Ask "List the 5 most common Python beginner mistakes. Format it as a table with columns: Mistake, Why It Happens, How to Fix It."

### JSON Output
Claude can return data as valid JSON you can use in code.

> **Try this:** Ask "Return a JSON object representing a user profile with fields for name, age, email, and a list of hobbies. Use realistic fake data."

### Step-by-Step Instructions
Claude can write numbered how-to guides on demand.

> **Try this:** Ask "Write step-by-step instructions for setting up a Python virtual environment on a Mac, for a complete beginner."

---

## System Prompts and Instructions

### Custom Instructions
You can give Claude a set of rules at the start of a conversation that shape every response.

> **Try this:** Start a new conversation with "For this conversation: always respond in bullet points, never use more than 3 bullets per answer, and end every response with a follow-up question." Then have a normal conversation and observe the behavior.

### Constraints and Rules
Claude follows explicit constraints you set — length limits, forbidden words, required formats.

> **Try this:** Say "Answer my next three questions in exactly two sentences each, no more, no less." Then ask three questions of different complexity.

### Personas
You can define a character for Claude to play consistently throughout a session.

> **Try this:** Say "You are Byte, a friendly Python tutor who only uses food analogies to explain programming concepts." Then ask "What is a variable?"

---

## Memory and Context (Advanced)

### Long Context Handling
Claude can hold and reason about large amounts of text in a single conversation.

> **Try this:** Paste the full contents of all your `.py` files into one message. Then ask "Which file would be the best place to add a logging utility function, and why?"

### Context Window Awareness
Claude knows when context might be getting long and can summarize or reset.

> **Try this:** After a long conversation, ask "Summarize everything we've discussed so far as a bullet-point list of decisions and conclusions."

### CLAUDE.md as Persistent Instructions
The `CLAUDE.md` file in your project is loaded automatically — it's how you give Claude standing instructions about your codebase.

> **Try this:** Add a new rule to your `CLAUDE.md` like "Always suggest type hints when writing Python functions." Then start a fresh session and ask Claude to write a function — see if it follows the rule.

---

## Agentic and Tool Use (Advanced)

### Multi-Step Tasks
Claude can plan and execute tasks that span multiple actions — reading files, running commands, editing code.

> **Try this:** Ask "Read all the Python files in this project, then tell me which functions are missing docstrings."

### File Editing
Claude can directly edit files in your project, not just suggest changes.

> **Try this:** Ask "Add a docstring to the `calculate_sum` function in `sum.py`."

### Shell Commands
Claude can run bash commands to inspect your environment, run tests, or build things.

> **Try this:** Ask "Run the test suite and tell me if everything passes" (after you've written some tests).

### Parallel Tool Use
Claude can call multiple tools at the same time when they don't depend on each other.

> **Try this:** Ask "At the same time, check the git log and list all Python files in this project. Then summarize both."

---

## Meta: Learning Claude Itself

### Asking About Capabilities
Claude can explain its own features, limitations, and how to use it effectively.

> **Try this:** Ask "What are the most common mistakes people make when prompting you, and how should they avoid them?"

### Prompt Engineering
You can ask Claude to help you write better prompts for Claude.

> **Try this:** Write a vague prompt like "Help me with my code." Then ask Claude "Rewrite this prompt to get a more useful response from you."

### Evaluating Output Quality
Claude can critique its own responses when asked.

> **Try this:** Ask Claude a question, get an answer, then ask "How confident are you in that answer, and what could make it wrong?"

---

*This guide is a living document — add new sections as you discover features worth exploring.*
# Workshop: Building and Analyzing AI Agents with AutoGen

## Overview

This exercise demonstrates a practical implementation of various AI agent patterns using the AutoGen framework. Through this workshop, we build several agents that cooperate to perform research-related tasks, including retrieving academic information from arXiv, evaluating research feedback, and incorporating up-to-date web results via Bing Search.

## Environment Setup

- The notebook installs and upgrades key packages:
  - `langchain-community`
  - `autogen-agentchat`
  - `autogen-ext`
  - `arxiv`
  - `colorama`
  - `python-dotenv`
  
These dependencies provide support for:
  - Language model interactions (Azure OpenAI)
  - Integrating external tool APIs like Bing Search and arXiv queries.
  - Display formatting and environment configuration.

## Agent Architecture and Patterns

### Agentic Reflection Pattern

In this paradigm, one or more agents reflect on the results of the research or analysis:
- **Researcher Agent:** Finds relevant articles and crafts an answer based on academic data.
- **Critic Agent:** Evaluates the researcher output, offering insight and constructive feedback.
  
This combination encourages agents to not only generate but also critique outputs—an essential element in iterative improvement.

### Team of Agents

Multiple agents interact in a group chat style (using `MagenticOneGroupChat`):
- Agents exchange messages, each contributing their specialized expertise.
- In some cells, a third agent (WebGrounding) supplements academic data with recent, real-time web facts.

### Human in the Loop Pattern

A further extension integrates human feedback:
- After agents produce initial research, a human user can select or add use cases.
- This ensures that the final output benefits from human context and judgment.

### LLM as a Judge Pattern

An extra task added in this exercise:
- An agent is wrapped with a judge functionality (`AgentWithJudge`).
- After a response is generated, this agent evaluates the overall performance with a quantitative score and explanation in JSON format.
- This pattern borrows from the Actor pattern in concurrent programming, where one agent not only acts but also assesses the output of another.

## Theoretical Background

### Actor Pattern (AutoGen)

Originating from concurrent computing, the actor pattern involves:
- Autonomous agents ("actors") that receive and process messages concurrently.
- In our context, each agent (Researcher, Critic, WebGrounding) functions independently, yet collaboratively, replicating the actor model.

### Reflection Pattern

The reflection pattern emphasizes:
- Self-analysis of an agent’s work, allowing iterative improvement.
- The researcher agent reflects on its work after the critic evaluates, ensuring continuous learning and performance tuning.

### Integration with External Tools

To perform specialized tasks, agents incorporate:
- **LangChainToolAdapter:** Wraps external API calls (e.g., Arxiv query, Bing Search) ensuring compatibility with AutoGen’s interface.
- **Azure OpenAI Chat Client:** Provides a backend for generating and refining agent responses.

## Summary

This comprehensive setup illustrates multiple agentic frameworks, showing how they can blend automated reasoning with human oversight. The exercise is designed to highlight:
- The modularity and adaptability of the AutoGen framework.
- The synergy between different agent roles.
- The significance of reflection and iterative evaluation in complex AI systems.

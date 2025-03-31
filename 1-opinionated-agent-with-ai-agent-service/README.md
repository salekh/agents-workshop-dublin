# Cryptocurrency Agent with Azure AI Agent Service

This exercise demonstrates how to integrate and interact with an AI-driven Cryptocurrency Agent using the Azure AI SDK. The notebook walks through essential steps required to configure, monitor, and communicate with the agent using a multi-step process.

## Table of Contents

- [Introduction](#introduction)
- [Setup & Dependencies](#setup--dependencies)
- [Tracing & Telemetry](#tracing--telemetry)
- [Agent Thread Creation & Execution](#agent-thread-creation--execution)
- [Theoretical Background on AI Agents](#theoretical-background-on-ai-agents)
- [Summary](#summary)

## Introduction

This notebook is designed to:
- Set up environment variables and dependencies.
- Configure telemetry and tracing to monitor operations.
- Initialize and communicate with a Cryptocurrency Agent.
- Perform multiple operations (running queries, retrieving outputs and images) dynamically using threads.

The aim is to showcase practical integration methods as well as provide insights into building AI-driven automation using cloud services.

## Setup & Dependencies

The notebook begins by installing the required Python packages:
- `azure-ai-projects` for interacting with Azure-backed AI projects.
- `azure-identity` to handle Azure authentication.
- `opentelemetry-api` and `azure-monitor-opentelemetry` for observability.
- Other helper libraries such as `python-dotenv` for managing environment variables and `rich` for formatted console output.

> **Note:** The environment variables, such as `AZURE_AI_AGENT_PROJECT_CONNECTION_STRING` and `AZURE_AI_CRYPTO_AGENT_ID`, are loaded from a `.env` file to securely manage secrets.

## Tracing & Telemetry

After setting up the environment, the notebook enables robust tracking with Azure Monitor:
- **Tracing:** By configuring OpenTelemetry, the process captures detailed execution spans.
- **Telemetry:** This provides insights and monitoring through Application Insights connecting via a telemetry connection string.

These mechanisms ensure that the agent activities are fully observable, which is crucial for debugging, performance tuning, and audit trails.

## Agent Thread Creation & Execution

The notebook demonstrates two key variants:

1. **Standard Query Execution:**
   - The agent is initialized using an assistant ID.
   - A communication thread is created.
   - A message is sent, instructing it to fetch the top 5 most traded cryptocurrencies and perform additional volume calculations.

2. **Extended Query with Visual Output:**
   - A new thread is started to request detailed OHLCV data for BTC.
   - The query asks for the generation of a candlestick chart, showing both textual and image outputs.
   - Messages returned from the agent are polled until a final answer is available. If an image is returned, it is saved locally.

These steps illustrate handling synchronous and asynchronous communication with an agent, including message polling and output extraction.

## Theoretical Background on AI Agents

AI Agents are autonomous or semi-autonomous programs designed to perform tasks by making decisions based on inputs. They can interact with human operators or other systems to:

- **Automate repetitive tasks:** By leveraging AI capabilities, agents can quickly process large amounts of data and reply to user queries.
- **Learn and adapt:** Modern AI Agents use machine learning models to understand context and improve over time.
- **Monitor operations:** Tools like telemetry and tracing (via frameworks such as OpenTelemetry) allow developers to monitor the system's performance and gain insights into behavioral patterns.
- **Integrate with Cloud Services:** Using cloud SDKs, developers can build scalable and resilient AI systems that manage tasks like financial data processing, customer support, or predictive analyses.

In this exercise, the Cryptocurrency Agent serves as a hands-on example of an AI-driven solution interfacing with Azure services to perform complex data extraction and visualization tasks.

## Summary

This exercise provided a comprehensive look at:
- Setting up an AI agent environment.
- Enabling and monitoring telemetry for improved observability.
- Managing agent threads to execute multiple tasks and extract both textual and visual outputs.
- Exploring theoretical concepts behind AI Agents, including automation, learning, and cloud integration.

By following these steps, users gain practical experience in leveraging AI agents within a modern cloud framework.

Happy Coding!

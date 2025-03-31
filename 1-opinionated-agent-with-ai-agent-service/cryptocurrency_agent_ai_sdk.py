# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
import time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from rich import print  # added for rich formatted output

load_dotenv()
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["AZURE_AI_AGENT_PROJECT_CONNECTION_STRING"],
)
# [START enable_tracing]
from opentelemetry import trace
from azure.monitor.opentelemetry import configure_azure_monitor

# Enable Azure Monitor tracing
application_insights_connection_string = (
    project_client.telemetry.get_connection_string()
)
if not application_insights_connection_string:
    print("[bold red]Application Insights was not enabled for this project.[/bold red]")
    print("[bold red]Enable it via the 'Tracing' tab in your AI Foundry project page.[/bold red]")
    exit()
configure_azure_monitor(connection_string=application_insights_connection_string)

# enable additional instrumentations
project_client.telemetry.enable()

scenario = os.path.basename(__file__)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span(scenario):
    with project_client:
        # [END enable_tracing]
        agent = project_client.agents.get_agent(
            assistant_id=os.environ["AZURE_AI_CRYPTO_AGENT_ID"]
        )
        print(f"[green]Fetching Cryptocurrency Agent with ID: {agent.id}[/green]")

        thread = project_client.agents.create_thread()
        print(f"[green]Created thread, thread ID: {thread.id}[/green]")

        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content="Find out the 5 most traded cryptocurrencies today."
            + "If that currency was traded on various exchanges,"
            + "calculate the sum of all trading volumes. "
            + "Also list the exchanges traded on, in a separate column.",
        )
        print(f"[green]Created message, message ID: {message.id}[/green]")

        run = project_client.agents.create_run(thread_id=thread.id, assistant_id=agent.id)

        # Poll the run as long as run status is queued or in progress
        while run.status in ["queued", "in_progress", "requires_action"]:
            # Wait for a second
            time.sleep(1)
            run = project_client.agents.get_run(thread_id=thread.id, run_id=run.id)
            print(f"[yellow]Run status: {run.status}[/yellow]")

        # Get all messages and print only the final assistant answer.
        messages = project_client.agents.list_messages(thread_id=thread.id)
        final_answer = next(
            (msg['content'][0]['text']['value'] for msg in messages['data']
             if msg['role'] == 'assistant' and msg.get('assistant_id')), 
            "No answer received"
        )
        print(f"[blue]Final answer: {final_answer}[/blue]")

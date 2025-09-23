import click

from clients.services import ClientService
from clients.models import Client
@click.group()
def clients():
    """
    Manages the clients lifecycle
    """
    pass

@clients.command()
@click.option('-n','--name',type = str,prompt=True,help="The Client name")
@click.option('-n','--company',type = str,prompt=True,help="The Clients company")
@click.option('-n','--email',type = str,prompt=True,help="The Clients email")
@click.option('-n','--position',type = str,prompt=True,help="The Clients position")
@click.pass_context
def create(ctx, name, company, email, position):
    """
    Creates a new client
    """
    client = Client(name,company,email,position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """
    List all clients
    """
    pass

@clients.command()
@click.pass_context
def updated(ctx, client_uid):
    """
    Updates a client
    """
    pass

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """
    Deletes a client
    """
    pass

all = clients

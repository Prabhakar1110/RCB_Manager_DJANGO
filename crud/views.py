from django.shortcuts import render, redirect, get_object_or_404
from .models import Player
from .forms import PlayerForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

#Create
def create_player(request):
    try:
        if request.method == "POST":
            rec = PlayerForm(request.POST, request.FILES)
            if rec.is_valid():
                p = rec.save()
                messages.success(request, f'"{p.name}" Created successfully!!')
                return redirect("crud:list_player")
            else:
                messages.error(request, 'Invalid form data')
                print("Form Errors:", rec.errors)  # Debugging
                return render(
                    request,
                    'crud/create_player.html',
                    {"form":rec},
                )
        else:
            form = PlayerForm()
            return render(
                request,
                'crud/create_player.html',
                {"form":form},
            )
    except Exception as e:
        messages.error(request, f'Unexpected Error while creating Player: {str(e)}')
        return redirect("crud:list_player")


#Read All
def list_player(request):
    try:
        all_players = Player.objects.prefetch_related("fav_food").all()
        return render(
            request,
            'crud/list_player.html',
            { "all_players":all_players },
        )
    except Exception as e:
        messages.error(request, f'Unexpected Error while fetching players: {str(e)}')
        return redirect("crud:list_player")

#Read one
def view_player(request, pk):
    # try:
        player = get_object_or_404(Player, pk=pk)
        return render(
            request,
            "crud/view_player.html",
            {"player":player},
        )
    # except Exception as e:
    #     messages.error(request, f'Unexpected Error while fetching player: {str(e)}')
    #     return redirect("crud:list_player")

#Update
def update_player(request, pk):
    try:
        player = get_object_or_404(Player, pk=pk)
        if request.method == "POST":
            form = PlayerForm(request.POST, request.FILES, instance=player)
            if form.is_valid():
                p = form.save()
                messages.success(request, f'"{p.name}" Updated successfully!!')
                return redirect("crud:list_player")
            else:
                messages.error(request, 'Invalid form data')
                print("Form Errors:", form.errors)  # Debugging
                return render(
                    request,
                    'crud/update_player.html',
                    {"form":form},
                )
        else:
            form = PlayerForm(instance=player)
            return render(
                request,
                "crud/update_player.html",
                {"form":form},
            )
    except Exception as e:
        messages.error(request, f"Error while Updating Player: {str(e)}")
        return redirect("crud:list_player")


#Delete
def delete_player(request, pk):
    try:
        player = get_object_or_404(Player, pk=pk)
        player_name = player.name  # Store before deletion
        player.delete()
        messages.success(request, f'"{player_name}" Deleted Successfully!')
        return redirect("crud:list_player")
    except Exception as e:
        messages.error(request, f"Unexpected Error while deleting: {str(e)}")
        return redirect("crud:list_player")

#create super user
def create_super(request):
    try:
        if not User.objects.filter(username="root").exists():
            User.objects.create_superuser("root", "", "root")
            return HttpResponse("Superuser created! Username: root, Password: root")
        return HttpResponse("Superuser already exists!")
    except Exception as e:
        messages.error(request, f"Unexpected Error while Creating SuperUser: {str(e)}")
        return redirect("crud:list_player")
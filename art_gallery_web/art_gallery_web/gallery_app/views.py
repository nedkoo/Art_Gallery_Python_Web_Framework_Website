from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


# from designs.forms import CreateDesignForm, PostForm
from art_gallery_web.core.cleaned_up_files import cleaned_up_files
from art_gallery_web.core.decorators import user_is_entry_author

from art_gallery_web.gallery_app.forms import CreateArtForm
from art_gallery_web.gallery_app.models import Arts


def list_arts(request):
    arts = Arts.objects.all()
    # for art in arts:
    #     art.can_delete = art.created_by_id == request.user.id
    #     art.can_edit = art.created_by_id == request.user.id

    context = {
        'arts': arts,
        'current_page': 'list_designs',

    }
    return render(request, 'arts/arts_list.html', context)


def details_arts(request, pk):
    art = Arts.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'art': art,
            'can_modify': art.created_by_id == request.user.id,
        }
        return render(request, 'arts/art_details.html', context)


def create_art(request):
    if request.method == "GET":
        form = CreateArtForm()
        context = {

            'form': form,

        }
        return render(request, 'arts/art_create.html', context)
    else:
        form = CreateArtForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save(commit=False)
            art.created_by_id = request.user.id
            art.save()

            return redirect('list arts')
        context = {

            'form': form,

        }
        return render(request, 'arts/art_create.html', context)



@login_required
@user_is_entry_author
def delete_art(request, pk):
    art = Arts.objects.get(pk=pk)
    # to delete only owner
    if art.created_by_id != request.user.id:
        return redirect('index')
    if request.method == "GET":

        context = {
            'art': art,

        }
        return render(request, 'arts/art_delete.html', context)
    else:

        art.delete()
        cleaned_up_files(art.image.path)

        return redirect('list arts')

@login_required
@user_is_entry_author
def edit_art(request, pk):
    art = Arts.objects.get(pk=pk)
    if request.method == "GET":
        form = CreateArtForm(instance=art)
        context = {
            'art': art,
            'form': form
        }
        return render(request, 'arts/art_edit.html', context)
    else:

        old_image = art.image

        form = CreateArtForm(request.POST, request.FILES, instance=art)
        if form.is_valid():
            if 'image' in request.FILES:
                cleaned_up_files(old_image.path)

            form.save()

            return redirect('list arts')
        context = {
            'art': art,
            'form': form
        }
        return render(request, 'arts/art_edit.html', context)

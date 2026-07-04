from django.shortcuts import render, redirect


def handle_create_form(request, form_class, template_name, redirect_name, context=None):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_name)
    else:
        form = form_class()
    ctx = {'form': form}
    if context:
        ctx.update(context)
    return render(request, template_name, ctx)


def handle_update_form(request, model_class, form_class, pk, template_name, redirect_name, context=None):
    instance = model_class.objects.get(id=pk)
    form = form_class(instance=instance)
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect(redirect_name)
    ctx = {'form': form}
    if context:
        ctx.update(context)
    return render(request, template_name, ctx)


def handle_delete(request, model_class, pk, redirect_name):
    instance = model_class.objects.get(id=pk)
    instance.delete()
    return redirect(redirect_name)


def handle_list(request, model_class, template_name, context_name):
    queryset = model_class.objects.all()
    return render(request, template_name, {context_name: queryset})

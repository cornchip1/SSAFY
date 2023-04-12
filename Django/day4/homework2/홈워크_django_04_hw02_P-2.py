def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect(request,'articles/index.html')
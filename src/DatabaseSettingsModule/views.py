"""
Documenting Hierarchy : First Documentation
----------------------
This is a Module which has Class for Database and database Settings

"""

#Function Based Views 
def movie_list(request):
    """
    This is GET method 
    """
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    


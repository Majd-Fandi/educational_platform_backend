from rest_framework import permissions

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_student

class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_instructor
    


# you can use these permissions in the views : 

# EX :

# from .permissions import IsInstructor

# class InstructorOnlyView(APIView):
#     permission_classes = [permissions.IsAuthenticated, IsInstructor]

#     def get(self, request):
#         return Response({"detail": "This view is for instructors only."})
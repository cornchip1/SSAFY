from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

#UserCreateForm 의 모든 것을 상속받는다
class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta) : 
        #UserCreationForm 내 Meta의 모든 class를 상속받는데, 그 중 model만 변경한다
        model = get_user_model()

#UserChangeForm 의 모든 것을 상속받는다
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta) : 
        #UserChangeForm 내 Meta의 모든 class를 상속받는데, 그 중 model만 변경한다
        model = get_user_model()
        fields = {'username','email', 'first_name','last_name'}
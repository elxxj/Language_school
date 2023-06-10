from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, CourseEdition, Teacher, Review
from .forms import StudentRegistrationForm
from .forms import ReviewForm
# Create your views here.


def home(request):
    """
    Wyświetla stronę główną mojego projektu - Language Sail Academy.
    """
    return render(request, 'home.html')


def about(request):
    """
    Wyświetla widok 'O nas', gdzie znajduje się krótki opis szkoły.
    """
    return render(request, 'about.html')


def courses_table(request):
    """
    Wyświetla widok 'Kursy', gdzie znajdują się dane o kursach (Kurs, Jezyk, Edycja kursu, Nauczyciele prowadzący).
    """
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses_table.html', context)


def course_edition_details(request, edition_id):
    """
    Wyświetla dane szczegółowe na temat danej edycji kursu.
    Dane to: opis o kursie, poziom, data rozpoczęcia kursu, data zakończenia kursu, nauczyciele prowadzący.
    """
    course_edition = CourseEdition.objects.get(id=edition_id)

    context = {
        'course_edition': course_edition
    }
    return render(request, 'course_edition_details.html', context)


def teacher_details(request):
    """
    Wyświetla widok 'Lektorzy', gdzie znajdują się dane dotyczące nauczycieli (ich bio i prowadzone przez nich kursy i edycje).
    """
    teachers = Teacher.objects.all()
    return render(request, 'teacher_details.html', {'teachers': teachers})


def review(request):
    """
    Wyświetla widok 'Opinie', gdzie student może zobaczyć opinie innych i dodać swoją własną opinię na temat szkoły jezykowej.
    """
    reviews = Review.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('review')
        else:
            form = ReviewForm()
        return render(request, 'review.html', {'form': form, 'reviews': reviews})
    else:
        return render(request, 'review.html', {'reviews': reviews})


def contact(request):
    """
    Wyświetla widok 'Kontakt', gdzie znajduja się dane kontaktowe do szkoły językowej (adres, telefon, mail, instagram).
    """
    return render(request, 'contact.html')


def student_registration(request):
    """
    Wyświetla widok 'Rejestracja', gdzie student może zarejestrować się do szkoły podając imię, nazwisko, nazwę użytkownika i hasło.
    """
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'student_registration.html', context)


@login_required
def profile(request):
    """
    Wyświetla profil studenta po wcześniejszym zalogowaniu się.
    """
    return render(request, 'profile.html')

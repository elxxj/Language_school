import pytest
from school_app.models import Course, CourseEdition, Language


@pytest.fixture
def prepared_data():
    language = Language.objects.create(name='Test Language')
    course = Course.objects.create(name='Test Course', language=language)
    course_edition = CourseEdition.objects.create(name='Test Course Edition', course=course)
    return {
        'language': language,
        'course': course,
        'course_edition': course_edition,
    }

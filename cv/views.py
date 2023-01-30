from django.shortcuts import render
from .models import CV,Link,Project,Certificate,Skill,Education,Work,Language
from .serializers import CvSerializers,LinkSerializers,ProjectSerializers,CertificateSerializers,SkillSerializers,EducationSerializers,WorkSerializers,LanguageSerializers
from rest_framework import generics

from django.shortcuts import get_object_or_404

# Create your views here.

# CV views

class CvList(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CvSerializers


class CvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CvSerializers

# Link views

class LinkListView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializers

    def get_queryset(self):
        if self.kwargs.get('cv_id'):
            return self.queryset.filter(cv_id=self.kwargs.get('cv_id'))
        return self.queryset.all()


class LinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializers

    def get_object(self):
        if self.kwargs.get('cv_id'):
            return get_object_or_404(self.get_queryset(), cv_id=self.kwargs.get('cv_id'),
                                     pk=self.kwargs.get('link_id'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('link_id'))

# Project views

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

    def get_queryset(self):
        if self.kwargs.get('cv_id'):
            return self.queryset.filter(cv_id=self.kwargs.get('cv_id'))
        return self.queryset.all()


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers

    def get_object(self):
        if self.kwargs.get('cv_id'):
            return get_object_or_404(self.get_queryset(), cv_id=self.kwargs.get('cv_id'),
                                     pk=self.kwargs.get('project_id'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('project_id'))

# Certificate views

class CertificateListView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializers

    def get_queryset(self):
        if self.kwargs.get('cv_id'):
            return self.queryset.filter(cv_id=self.kwargs.get('cv_id'))
        return self.queryset.all()


class CertificateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializers

    def get_object(self):
        if self.kwargs.get('cv_id'):
            return get_object_or_404(self.get_queryset(), cv_id=self.kwargs.get('cv_id'),
                                     pk=self.kwargs.get('certificate_id'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('certificate_id'))

# Skill views

class SkillListView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers

    def get_queryset(self):
        if self.kwargs.get('cv_id'):
            return self.queryset.filter(cv_id=self.kwargs.get('cv_id'))
        return self.queryset.all()


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers

    def get_object(self):
        if self.kwargs.get('cv_id'):
            return get_object_or_404(self.get_queryset(), cv_id=self.kwargs.get('cv_id'),
                                     pk=self.kwargs.get('skill_id'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('skill_id'))

# Education views

class EducationListView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers

    def get_queryset(self):
        if self.kwargs.get('cv_id'):
            return self.queryset.filter(cv_id=self.kwargs.get('cv_id'))
        return self.queryset.all()


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers

    def get_object(self):
        if self.kwargs.get('cv_id'):
            return get_object_or_404(self.get_queryset(), cv_id=self.kwargs.get('cv_id'),
                                     pk=self.kwargs.get('education_id'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('education_id'))

# Work views

class WorkListView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers

    def get_queryset(self):
        if self.kwargs.get('cv_id'):
            return self.queryset.filter(cv_id=self.kwargs.get('cv_id'))
        return self.queryset.all()


class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers

    def get_object(self):
        if self.kwargs.get('cv_id'):
            return get_object_or_404(self.get_queryset(), cv_id=self.kwargs.get('cv_id'),
                                     pk=self.kwargs.get('work_id'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('work_id'))

# Language views

class LanguageListView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers

    def get_queryset(self):
        if self.kwargs.get('cv_id'):
            return self.queryset.filter(cv_id=self.kwargs.get('cv_id'))
        return self.queryset.all()


class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers

    def get_object(self):
        if self.kwargs.get('cv_id'):
            return get_object_or_404(self.get_queryset(), cv_id=self.kwargs.get('cv_id'),
                                     pk=self.kwargs.get('language_id'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('language_id'))


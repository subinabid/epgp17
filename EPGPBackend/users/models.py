"""User models"""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  # type: ignore
from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore
from .managers import UserManager  # type: ignore

STATES = (
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CG", "Chhattisgarh"),
    ("DL", "Delhi"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JK", "Jammu and Kashmir"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OD", "Odisha"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TG", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UK", "Uttarakhand"),
    ("WB", "West Bengal"),
    ("AN", "Andaman and Nicobar Islands"),
    ("CH", "Chandigarh"),
    ("DN", "Dadra and Nagar Haveli"),
    ("DD", "Daman and Diu"),
    ("LD", "Lakshadweep"),
    ("PY", "Puducherry"),
)

STUDY_CENTER_STATES = (
    ("BR", "Bihar"),
    ("CG", "Chhattisgarh"),
    ("CH", "Chandigarh"),
    ("DL", "Delhi"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("MH", "Maharashtra"),
    ("MP", "Madhya Pradesh"),
    ("OD", "Odisha"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("TG", "Telangana"),
    ("TN", "Tamil Nadu"),
    ("UK", "Uttarakhand"),
    ("UP", "Uttar Pradesh"),
    ("WB", "West Bengal"),
)

STUDY_CENTER_CITIES = {
    "BR": ("Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Purnia"),
    "CG": ("Raipur", "Bhilai", "Bilaspur", "Korba", "Durg"),
    "CH": ("Chandigarh"),
    "DL": ("New Delhi"),
    "GA": ("Panaji", "Vasco da Gama", "Margao", "Mapusa", "Ponda"),
    "GJ": ("Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar"),
    "HR": ("Faridabad", "Gurugram", "Panipat", "Ambala", "Yamunanagar"),
    "JH": ("Ranchi", "Jamshedpur", "Dhanbad", "Bokaro Steel City", "Deoghar"),
    "KA": ("Bengaluru", "Mangaluru"),
    "KL": ("Thiruvananthapuram", "Kochi", "Kozhikode"),
    "MH": ("Mumbai", "Pune", "Nagpur", "Thane", "Nashik"),
    "MP": ("Indore", "Bhopal", "Jabalpur", "Gwalior", "Ujjain"),
    "OD": ("Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur", "Puri"),
    "PB": ("Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda"),
    "RJ": ("Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer"),
    "TG": ("Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Ramagundam"),
    "TN": ("Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"),
    "UK": ("Dehradun", "Haridwar", "Roorkee", "Haldwani", "Kashipur"),
    "UP": ("Lucknow", "Kanpur", "Ghaziabad", "Agra", "Meerut"),
    "WB": ("Kolkata", "Asansol", "Siliguri", "Durgapur", "Bardhaman"),
}


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    personalEmail = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)
    homeState = models.CharField(max_length=100, null=True, blank=True, choices=STATES)
    homeTown = models.CharField(max_length=100, null=True)
    currentCity = models.CharField(max_length=100, null=True)
    studyCenterState = models.CharField(
        max_length=100, choices=STUDY_CENTER_STATES, default="KL"
    )
    studyCenterCity = models.CharField(max_length=100, null=True)
    studyCenterName = models.CharField(max_length=100, null=True)
    employer = models.CharField(max_length=100, null=True)
    jobTitle = models.CharField(max_length=100, null=True)
    linkedIn = models.URLField(null=True)
    facebook = models.URLField(null=True)
    twitter = models.URLField(null=True)
    instagram = models.URLField(null=True)
    github = models.URLField(null=True)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

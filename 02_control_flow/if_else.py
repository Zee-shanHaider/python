age = 20

if age >= 18:
    print("adult")
else:
    print("minor")

score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("admin dashboard")
elif is_logged_in:
    print("user dashboard")
else:
    print("login required")

num = 7
print("odd" if num % 2 != 0 else "even")

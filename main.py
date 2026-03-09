from pyscript import display, document

def intramurals_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    document.getElementById('leader').innerHTML = ' '

    registration_input = document.querySelector('input[name="registration"]:checked')
    clearance_input = document.querySelector('input[name="clearance"]:checked')

    if registration_input is None:
        display("Please select your registration status.", target="output")
        return
    if clearance_input is None:
        display("Please select your medical clearance.", target="output")
        return

    registration = registration_input.value
    clearance = clearance_input.value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value
    registration_input = document.querySelector('input[name="registration"]:checked')
    clearance_input = document.querySelector('input[name="clearance"]:checked')
    registration = registration_input.value

    if registration != 'registered':
        display(f'Not eligible: student is not registered for intramurals. Please register online.', target='output')
    elif clearance != 'cleared':
        display(f'Not eligible: medical clearance required. Please get cleared before participating.', target='output')
# from lines 31 to 130 this is used for the image and elif mechhanics for the intramurals team selection
    elif grade_level == 7:
        if section == "red":
            display(f'Congratulations! You are assigned to the Red Bulldogs!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="red bulldogs.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "blue":
            display(f'Congratulations! You are assigned to the Blue Bears!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="blue bears.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "yellow":
            display(f'Congratulations! You are assigned to the Yellow Tigers!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="yellow tigers.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "green":
            display(f'Congratulations! You are assigned to the Green Hornets!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="green hornets.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
    elif grade_level == 8:
        if section == "red":
            display(f'Congratulations! You are assigned to the Red Bulldogs!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="red bulldogs.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "blue":
            display(f'Congratulations! You are assigned to the Blue Bears!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="blue bears.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "yellow":
            display(f'Congratulations! You are assigned to the Yellow Tigers!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="yellow tigers.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "green":
            display(f'Congratulations! You are assigned to the Green Hornets!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="green hornets.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
    elif grade_level == 9:
        if section == "red":
            display(f'Congratulations! You are assigned to the Red Bulldogs!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="red bulldogs.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "blue":
            display(f'Congratulations! You are assigned to the Blue Bears!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="blue bears.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "yellow":
            display(f'Congratulations! You are assigned to the Yellow Tigers!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="yellow tigers.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "green":
            display(f'Congratulations! You are assigned to the Green Hornets!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="green hornets.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
    elif grade_level == 10: 
        if section == "red":
            display(f'Congratulations! You are assigned to the Red Bulldogs!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="red bulldogs.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "blue":
            display(f'Congratulations! You are assigned to the Blue Bears!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="blue bears.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "yellow":
            display(f'Congratulations! You are assigned to the Yellow Tigers!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="yellow tigers.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
        elif section == "green":
            display(f'Congratulations! You are assigned to the Green Hornets!', target='output')
            document.getElementById("image").innerHTML = """
            <img src="green hornets.jpg" width="300">
            """
            display(f'Good luck!', target='leader')
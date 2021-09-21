import os

os.chdir('\Users\steph\Desktop\Python_Files_Rename\Planets')

print(os.getcwdb)

for f in os.listdir():
    print(f)
    print(os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
    print(f_name.split('-'))

    f_title, f_course, f_num = _name.split('-')
    print(f_title)

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = ('{}-{}{}'.format(f_num, f_title, f_ext))

    os.rename(f, new_name)



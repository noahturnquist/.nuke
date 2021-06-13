#Set backdrops to border and random desaturated colour
import nuke
import random


def backdrop_setter():

    for i in nuke.allNodes('BackdropNode'):
        if i['appearance'].value() != 'Border':
            i['appearance'].setValue('Border')
            z = random.uniform(0, 0.5)
            i['tile_color'].setValue((int('%02x%02x%02x%02x' % (z*255, z*255, z*255, 1), 16)))

        i_label = i['label'].value()
        i_list = i_label.split(' ')
        new_label = ''
        for word in i_list:
            if len(word) > 2:
                new_word = word.title()
                new_label += new_word + ' '
            else:
                new_label += word + ' '
        i['label'].setValue(new_label)


nuke.menu("Nuke").addCommand("Workflow/Set Backdrops", 'backdrops_setter.backdrop_setter')
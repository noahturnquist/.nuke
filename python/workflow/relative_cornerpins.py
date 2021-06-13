import nuke


def relative_cornerpins():
    cornerpin = nuke.selectedNode()

    try:
        for i in range(1, 5):
            cornerpin['from' + str(i)].clearAnimated()
            print ("Animation Deleted")
    except AttributeError:
        pass


    for i in range(1, 5):
        to = cornerpin['to' + str(i)].value()
        cornerpin['from' + str(i)].setValue(to)


    current_frame = nuke.frame()

    current_label_lst = cornerpin['label'].value().lower().replace(' ', '\n').split('\n')

    programs = ['nuke', 'mocha']
    program = None
    for prog in programs:
        if prog in current_label_lst:
            program = prog

    label = '{}\nx{}'.format(program.upper(), current_frame)
    cornerpin['label'].setValue(label)

nuke.menu("Nuke").addCommand("Workflow/Relative Cornerpin", 'relative_cornerpins/relative_cornerpins()')
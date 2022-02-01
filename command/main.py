from commands import Write, DeleteBySpaces, Short, Paste, Batch, Copy
from controller import TextController
from text import Text

def main() -> None:

    text = Text()

    controller = TextController()


    # controller.execute(Write(text=text, data='Hola que tal '))
    # controller.execute(Write(text=text, data='¿tu como estas? '))
    # controller.undo()
    # controller.redo()

    # controller.execute(DeleteBySpaces(text=text, spaces=4))
    # controller.execute(DeleteBySpaces(text=text, spaces=4))
    # controller.undo()
    # controller.undo()
    # controller.redo()

    # controller.execute(Short(text=text))
    # controller.undo()

    # controller.execute(Copy(text=text))

    # controller.execute(Paste(text=text))
    # controller.execute(Paste(text=text))
    # controller.execute(Paste(text=text))
    # controller.undo()
    # controller.redo()
    # controller.undo()
    # controller.undo()
    # controller.redo()

    controller.execute(
        Batch(
            commands= [
                Write(text=text, data='Hola que tal tu como estas? '),
                Write(text=text, data='dime si eres feliz, '),
                Write(text=text, data='porque ya yo me rendi '),
                DeleteBySpaces(text=text, spaces=6),
                DeleteBySpaces(text=text, spaces=3),
                Short(text=text),
                Paste(text=text),
                Paste(text=text),
                Paste(text=text)
            ]
        )
    )

    print('Aca empiezan los undo')
    controller.undo()
    print('Aca empiezan los redo')
    controller.redo()

if __name__ == '__main__':
    main()
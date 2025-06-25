from views.mainView import MainView


# Main function to run the application
def main():
    # Create the main view
    mainView = MainView()
    # Start the application
    mainView.getUI().mainloop()

main()
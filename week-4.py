import java.util.Scanner;

public class TextAdventureGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Mysterious Island Adventure!");
        System.out.println("You find yourself on a mysterious island. Your goal is to survive and escape.");

        // Start of the game
        System.out.println("You are standing at the crossroads. You can go left or right.");

        // Game loop
        while (true) {
            System.out.print("Enter your choice (left/right): ");
            String userChoice = scanner.nextLine().toLowerCase();

            // Process user choices
            switch (userChoice) {
                case "left":
                    System.out.println("You chose to go left.");
                    exploreLeftPath();
                    break;
                case "right":
                    System.out.println("You chose to go right.");
                    exploreRightPath();
                    break;
                default:
                    System.out.println("Invalid input. Please enter 'left' or 'right'.");
            }
        }
    }

    private static void exploreLeftPath() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("You encounter a dense forest. Do you want to explore deeper or go back?");

        System.out.print("Enter your choice (explore/back): ");
        String userChoice = scanner.nextLine().toLowerCase();

        switch (userChoice) {
            case "explore":
                System.out.println("You find a hidden treasure in the forest! Congratulations!");
                endGame();
                break;
            case "back":
                System.out.println("You decide to go back to the crossroads.");
                break;
            default:
                System.out.println("Invalid input. Please enter 'explore' or 'back'.");
        }
    }

    private static void exploreRightPath() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("You come across a dangerous cave. Do you want to enter or find another way?");

        System.out.print("Enter your choice (enter/find): ");
        String userChoice = scanner.nextLine().toLowerCase();

        switch (userChoice) {
            case "enter":
                System.out.println("You encounter a dragon inside the cave! Game over.");
                endGame();
                break;
            case "find":
                System.out.println("You decide to find another way around the cave.");
                endGame();
                break;
            default:
                System.out.println("Invalid input. Please enter 'enter' or 'find'.");
        }
    }

    private static void endGame() {
        System.out.println("Thanks for playing the Mysterious Island Adventure! Game Over.");
        System.exit(0);
    }
}


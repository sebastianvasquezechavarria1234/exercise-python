import sys
import patient_registry
import order_system
import water_consumption

def main():
    while True:
        print("\n" + "="*30)
        print("   PYTHON EXERCISES SUITE")
        print("="*30)
        print("1 - Patient Registry System")
        print("2 - Order & Stock System")
        print("3 - Water Consumption Tracker")
        print("0 - Exit")
        
        choice = input("\nSelect an exercise to run: ").strip()
        
        if choice == "1":
            patient_registry.main()
        elif choice == "2":
            order_system.main()
        elif choice == "3":
            water_consumption.main()
        elif choice == "0":
            print("Exiting suite. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()

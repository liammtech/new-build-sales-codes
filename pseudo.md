1. Accept a new build buying code
2. Query relevant info from system and return - display code's headline info on UI
3. Validate whether it is a new build buying code
4. Generate a suggested sales code (check no existing record)
5. Offer user chance to edit/overwrite the suggested sales code (check no existing record)
6. Query previous instances of that sales code prefix, and return an array of unique zInvExtra.ProductType values
7. Give user option to select between them as a dropdown
8. If no prior instance, prompt user for ProductType value
9. Validate whether valid ProductType entered
10. "Generate" button -> create new stock code by combining "constants" with "dependent" datafields
    - App will have a "defaults" object to read constants from
    - Dependent values:
        * Created user's name
        * Stock code
        * Description
        * LongDesc
        * Date fields
        * Linked item etc.
11. Post to system
12. Dialog for stock code summary print out
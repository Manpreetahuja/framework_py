Feature: Recognize FB logo
    @E2E
    Scenario: locate FB logo
        Given user launches chromebowser
        When launches facebook
        Then facebook logo is visible 
        And close the browser

     @Smoke
    Scenario: view FB logo
        Given user launches chromebowser
        When launches facebook
        Then facebook logo is visible 
        And close the browser

    

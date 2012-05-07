Feature: Loading a SNP from a recent GWAS study
In order to make sure that the GWAS recent studies include valid SNP data
As a user
I should be able to follow a link to a SNP from a study and see referenced PubMed articles

Scenario: Finding a SNP from the latest GWAS study
    Given I am on the disease browser page
    When I look around
    I should see a study with SNPs referenced
    When I click on the link for the first SNP
    Then I should see the SNP query results page for that SNP
    And I should see dbSNP results anywhere on the page

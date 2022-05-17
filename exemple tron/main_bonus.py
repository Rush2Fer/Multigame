from classes_bonus import Jeu

import pygame
pygame.init()
clock = pygame.time.Clock()

NOIR = pygame.Color(0, 0, 0)

def main():
    jeu = Jeu()

    while not jeu.pret:
        jeu.update_events()
        jeu.resolution_events_menu()
        
        jeu.affichage_menu()
        
        pygame.display.flip()
        
    while not jeu.fin_partie():
        jeu.screen.fill(NOIR)
        jeu.prepare_manche()
        jeu.affiche_jeu()
        pygame.display.flip()
        jeu.attendre_espace()
    
        while not jeu.fin_manche():
            jeu.update_events()
            jeu.resolution_events_jeu()

            jeu.screen.fill(NOIR)
            
            jeu.affiche_jeu()
            
            jeu.update_direction_joueurs()
            
            jeu.avancer_joueurs()
            jeu.check_collisions_j2j()
            jeu.check_collisions_j2b()
            
            jeu.update_bonus()
                
            pygame.display.flip()
            
            jeu.compteur += 1
            
            clock.tick(60)
            
        jeu.affiche_score()
        pygame.display.flip()
        jeu.attendre_espace()
    
    jeu.affiche_score()
    jeu.affiche_gagnant()
    pygame.display.flip()
    jeu.attendre_espace()
    del jeu
    main()
    
main()
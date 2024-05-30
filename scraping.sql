-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 30 mai 2024 à 03:30
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `scraping`
--

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `id` int(11) NOT NULL,
  `nom` varchar(128) NOT NULL,
  `description` varchar(512) DEFAULT NULL,
  `localisation` varchar(128) DEFAULT NULL,
  `propos` varchar(512) DEFAULT NULL,
  `metier` varchar(128) DEFAULT NULL,
  `entreprise` varchar(128) DEFAULT NULL,
  `expe_date` varchar(32) DEFAULT NULL,
  `ecole` varchar(128) DEFAULT NULL,
  `formation` varchar(128) DEFAULT NULL,
  `formation_date` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`id`, `nom`, `description`, `localisation`, `propos`, `metier`, `entreprise`, `expe_date`, `ecole`, `formation`, `formation_date`) VALUES
(1, 'giovanni verdy', '--', 'Perpignan, Occitanie, France', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'Samuel Etienne', 'Reporter and Producer at Bloomberg', 'Londres et périphérie, Royaume-Uni', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'Samuel Etienne', 'Reporter and Producer at Bloomberg', 'Londres et périphérie, Royaume-Uni', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'John Smith', NULL, 'Amsterdam, Hollande Septentrionale, Pays-Bas', '', NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'John Smith', NULL, 'Londres, Angleterre, Royaume-Uni', '', NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'John Smith', NULL, 'Houston et périphérie', '', NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'John Smith', NULL, 'Amsterdam, Hollande Septentrionale, Pays-Bas', '', NULL, NULL, NULL, NULL, NULL, NULL),
(8, 'John Smith', NULL, 'Londres, Angleterre, Royaume-Uni', '', NULL, NULL, NULL, NULL, NULL, NULL),
(9, 'Jimmy DECLERCQ', 'Etudiant en informatique', 'Perpignan, Occitanie, France', NULL, 'Intégrateur Web', 'La Bonne Com - Agence de Communication Digitale/Web - Perpignan', 'janv. 2024 - févr. 2024', 'Lycée Jean-Lurçat', 'BTS services informatiques aux organisations\nComputer Science', '2022 - 2024'),
(10, 'Antoine Petit', NULL, 'Bourgogne-Franche-Comté, France', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11, 'Antoine Petit', NULL, 'Bourgogne-Franche-Comté, France', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, 'John Petit', NULL, 'Paris et périphérie', NULL, 'Directeur des opérations', 'GROUPE BSL Sécurité', 'oct. 2021', NULL, NULL, NULL),
(13, 'S’inscrire sur LinkedIn', NULL, 'Paris et périphérie', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(14, 'S’inscrire sur LinkedIn', NULL, 'Paris et périphérie', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15, 'Jimmy DECLERCQ', 'Etudiant en informatique', 'Perpignan, Occitanie, France', NULL, 'Intégrateur Web', 'La Bonne Com - Agence de Communication Digitale/Web - Perpignan', 'janv. 2024 - févr. 2024', 'Lycée Jean-Lurçat', 'BTS services informatiques aux organisations\nComputer Science', '2022 - 2024');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

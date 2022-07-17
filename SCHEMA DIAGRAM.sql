--Active: 1657696784582@@localhost@3306@school
CREATE TABLE `student` (
  `id` int PRIMARY KEY,
  `names` text,
  `intake_student` text,
  `sex` text
);

CREATE TABLE `entrance` (
  `student_id` int,
  `intake_id` int
);

CREATE TABLE `intakes` (
  `id` int PRIMARY KEY,
  `intake` text,
  `number_students` int
);

CREATE TABLE `course` (
  `dept_no` int,
  `intake_id` int
);

CREATE TABLE `department` (
  `id` int PRIMARY KEY,
  `departments` text,
  `intake_id_available` int
);

ALTER TABLE `student` ADD FOREIGN KEY (`intake`) REFERENCES `intakes` (`intake`);

ALTER TABLE `entrance` ADD FOREIGN KEY (`student_id`) REFERENCES `student` (`id`);

ALTER TABLE `entrance` ADD FOREIGN KEY (`intake_id`) REFERENCES `intakes` (`id`);

ALTER TABLE `course` ADD FOREIGN KEY (`dept_no`) REFERENCES `department` (`id`);

ALTER TABLE `course` ADD FOREIGN KEY (`intake_id`) REFERENCES `intakes` (`id`);

ALTER TABLE `department` ADD FOREIGN KEY (`intake_id_available`) REFERENCES `intakes` (`id`);

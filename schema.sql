--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.3
-- Dumped by pg_dump version 9.4.3
-- Started on 2016-02-06 19:27:27 EST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 174 (class 3079 OID 12123)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2267 (class 0 OID 0)
-- Dependencies: 174
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 173 (class 1259 OID 491303)
-- Name: twats; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE twats (
    id integer NOT NULL,
    text text,
    location character varying(255),
    search character varying(255),
    tweeted_at timestamp without time zone
);


--
-- TOC entry 172 (class 1259 OID 491301)
-- Name: twats_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE twats_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2268 (class 0 OID 0)
-- Dependencies: 172
-- Name: twats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE twats_id_seq OWNED BY twats.id;


--
-- TOC entry 2148 (class 2604 OID 491306)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY twats ALTER COLUMN id SET DEFAULT nextval('twats_id_seq'::regclass);


--
-- TOC entry 2150 (class 2606 OID 491311)
-- Name: twats_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY twats
    ADD CONSTRAINT twats_pkey PRIMARY KEY (id);


--
-- TOC entry 2266 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM travis;
GRANT ALL ON SCHEMA public TO travis;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2016-02-06 19:27:27 EST

--
-- PostgreSQL database dump complete
--

